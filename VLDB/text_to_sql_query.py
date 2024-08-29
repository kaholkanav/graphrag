import sqlite3
import logging
from dotenv import load_dotenv
from neo4j import GraphDatabase
import ollama
import os
import networkx as nx
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])
class GraphDatabaseHandler:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])

    def close(self):
        self.driver.close()

    # def create_metadata_graph(self, metadata):
    #     with self.driver.session() as session:
    #         for table, columns in metadata.items():
    #             self.logger.debug(f"Creating node for table: {table}")
    #             session.run("CREATE (t:Table {name: $table_name})", table_name=table)
    #             for column, column_type in columns.items():
    #                 self.logger.debug(f"Creating node for column: {column} of type {column_type} in table {table}")
    #                 session.run("""
    #                     MATCH (t:Table {name: $table_name})
    #                     CREATE (t)-[:HAS_COLUMN]->(c:Column {name: $column_name, type: $column_type})
    #                 """, table_name=table, column_name=column, column_type=column_type)

    def create_metadata_graph(self, metadata):
        with self.driver.session() as session:
            column_map = {}
            
            # Limit to 5 tables
            limited_metadata = dict(list(metadata.items())[:5])
            
            for table, columns in limited_metadata.items():
                self.logger.debug(f"Creating node for table: {table}")
                session.run("CREATE (t:Table {name: $table_name})", table_name=table)
                
                # Limit to 10 columns per table
                limited_columns = dict(list(columns.items())[:10])
                
                for column, column_type in limited_columns.items():
                    self.logger.debug(f"Creating node for column: {column} of type {column_type} in table {table}")
                    session.run("""
                        MATCH (t:Table {name: $table_name})
                        CREATE (t)-[:HAS_COLUMN]->(c:Column {name: $column_name, type: $column_type})
                    """, table_name=table, column_name=column, column_type=column_type)
                    
                    # Store the column in the map to check for repetition or keys
                    if column not in column_map:
                        column_map[column] = [(table, column_type)]
                    else:
                        # If the column is repeated, create a relationship between the columns
                        for existing_table, existing_type in column_map[column]:
                            self.logger.debug(f"Creating relationship between {existing_table}.{column} and {table}.{column}")
                            session.run("""
                                MATCH (c1:Column {name: $column_name, type: $column_type}), 
                                    (c2:Column {name: $column_name, type: $existing_type})
                                WHERE c1 <> c2
                                CREATE (c1)-[:KEY_RELATION]->(c2)
                            """, column_name=column, column_type=column_type, existing_type=existing_type)
                        
                        column_map[column].append((table, column_type))

    def execute_query(self, query):
        with self.driver.session() as session:
            result = session.run(query)
            return [record for record in result]
    
    def get_transactions(self):
        with self.driver.session() as session:
            result = session.read_transaction(self._get_and_return_transactions)
            return result

    @staticmethod
    def _get_and_return_transactions(tx):
        query = (
            "MATCH (c:Customer)-[:MADE]->(t:Transaction)<-[:INVOLVED_IN]-(a:Account) "
            "RETURN c.CustomerID AS customer_id, t.TransactionID AS transaction_id, "
            "a.AccountID AS account_id, t.TransactionDate AS transaction_date, "
            "t.TransactionType AS transaction_type, t.TransactionAmount AS transaction_amount"
        )
        result = tx.run(query)
        return [(record["customer_id"], record["transaction_id"], record["account_id"],
                 record["transaction_date"], record["transaction_type"], record["transaction_amount"])
                for record in result]

def extract_metadata(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    metadata = {}
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        metadata[table_name] = {column[1]: column[2] for column in columns}
    conn.close()
    return metadata

logger = logging.getLogger(__name__)
def text_to_sql(natural_language_query):
    
    model_name = "llama2"  # Example model name, replace with the actual model name you are using
    prompt = f"Generate only the SQL query for the following request: {natural_language_query}. The output must be only the SQL query without any additional text, explanations, or formatting. Put the query inside curly braces {{}}. The query should be compatible with SQLite. SQLite uses the PRAGMA table_info command to get column information, so use that if relevant."
    response = ollama.generate(model=model_name, prompt=prompt)
    logger.debug(f"Response from model: {response}")  # Debugging line to inspect the response
    sql_query = response['response'].replace('```', '').strip()
    logger.debug(f"Generated SQL query: {sql_query}")
    if '{' in sql_query:
        #remove the curly braces from the response
        sql_query = sql_query[1:]
    if '}' in sql_query:
        sql_query = sql_query[:-1]
    return sql_query  # Remove the curly braces from the response

def execute_sql_on_sqlite(db_path, sql_query):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check if the query is a PRAGMA query (used for getting column information)
    if "PRAGMA" in sql_query.upper():
        table_name = sql_query.split('(')[1].split(')')[0].replace("'", "").replace('"', '').strip()
        cursor.execute(f"PRAGMA table_info({table_name})")
        result = cursor.fetchall()
        conn.close()
        # Extract and return the column names
        columns = [row[1] for row in result]  # Column names are in the second position of each row
        return columns
    else:
        # Execute normal SQL queries (e.g., SELECT * FROM table_name)
        cursor.execute(sql_query)
        result = cursor.fetchall()
        conn.close()
        return result

def visualize_graph(transactions):
    G = nx.Graph()

    for transaction in transactions:
        customer_id, transaction_id, account_id, transaction_date, transaction_type, transaction_amount = transaction
        G.add_node(customer_id, label='Customer')
        G.add_node(transaction_id, label='Transaction', date=transaction_date, type=transaction_type, amount=transaction_amount)
        G.add_node(account_id, label='Account')
        G.add_edge(customer_id, transaction_id, relationship='MADE')
        G.add_edge(account_id, transaction_id, relationship='INVOLVED_IN')

    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'relationship')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()


# Usage
db_path = 'banking_system.db'
metadata = extract_metadata(db_path)

#load env
load_dotenv()
uri=os.getenv('NEO4J_URI')
user=os.getenv('NEO4J_USER')
password=os.getenv('NEO4J_PASSWORD')
logger.debug(f"uri: {uri} user: {user} password: {password}")

neo4j_handler = GraphDatabaseHandler(uri, user, password)
neo4j_handler.create_metadata_graph(metadata)

# Convert natural language query to SQL
natural_language_query = "Show me all data of the Customer_Transaction_History table"
sql_query = text_to_sql(natural_language_query)
logger.debug(f" the sql query is {sql_query[1:-2]}")  # Print the generated SQL query to verify it

# Execute the SQL query on SQLite
result = execute_sql_on_sqlite(db_path, sql_query)
logger.debug(result)

#iterative query

# Close the Neo4j handler
neo4j_handler.close()

#visualizing the graph
load_dotenv()
uri=os.getenv('NEO4J_URI')
user=os.getenv('NEO4J_USER')
password=os.getenv('NEO4J_PASSWORD')
logging.debug(f"Connecting to Neo4j database at {uri} with user {user}")
graph_db_handler = GraphDatabaseHandler(uri, user, password)
transactions = graph_db_handler.get_transactions()
graph_db_handler.close()

visualize_graph(transactions)
