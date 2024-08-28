import sqlite3
from neo4j import GraphDatabase
import ollama

class GraphDatabaseHandler:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_metadata_graph(self, metadata):
        with self.driver.session() as session:
            for table, columns in metadata.items():
                print(f"Creating node for table: {table}")
                session.run("CREATE (t:Table {name: $table_name})", table_name=table)
                for column, column_type in columns.items():
                    print(f"Creating node for column: {column} of type {column_type} in table {table}")
                    session.run("""
                        MATCH (t:Table {name: $table_name})
                        CREATE (t)-[:HAS_COLUMN]->(c:Column {name: $column_name, type: $column_type})
                    """, table_name=table, column_name=column, column_type=column_type)

    def execute_query(self, query):
        with self.driver.session() as session:
            result = session.run(query)
            return [record for record in result]

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

def text_to_sql(natural_language_query):
    model_name = "llama2"  # Example model name, replace with the actual model name you are using
    prompt = f"Generate only the SQL query for the following request: {natural_language_query}. The output must be only the SQL query without any additional text, explanations, or formatting. Put the query inside curly braces {{}}. The query should be compatible with SQLite. SQLite uses the PRAGMA table_info command to get column information, so use that if relevant."
    response = ollama.generate(model=model_name, prompt=prompt)
    print(f"Response from model: {response}")  # Debugging line to inspect the response
    sql_query = response['response'].replace('```', '').strip()
    print(f"Generated SQL query: {sql_query}")
    return sql_query

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

# Usage
db_path = 'banking_system.db'
metadata = extract_metadata(db_path)

neo4j_handler = GraphDatabaseHandler("bolt://localhost:7687", "neo4j", "password")
neo4j_handler.create_metadata_graph(metadata)

# Convert natural language query to SQL
natural_language_query = "Show me all data of the Customer_Transaction_History table"
sql_query = text_to_sql(natural_language_query)
print(f" the sql query is {sql_query[1:-2]}")  # Print the generated SQL query to verify it

# Execute the SQL query on SQLite
result = execute_sql_on_sqlite(db_path, sql_query)
print(result)

#iterative query

# Close the Neo4j handler
neo4j_handler.close()
