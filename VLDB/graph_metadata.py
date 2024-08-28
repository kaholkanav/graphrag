from neo4j import GraphDatabase
import sqlite3
from dotenv import load_dotenv
import os

class GraphDatabaseHandler:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_metadata_graph(self, metadata):
        with self.driver.session() as session:
            for table, columns in metadata.items():
                session.write_transaction(self._create_table_node, table)
                for column in columns:
                    session.write_transaction(self._create_column_node, table, column)

    @staticmethod
    def _create_table_node(tx, table):
        tx.run("MERGE (t:Table {name: $table})", table=table)

    @staticmethod
    def _create_column_node(tx, table, column):
        column_name, column_type = column[1], column[2]
        tx.run("""
            MATCH (t:Table {name: $table})
            MERGE (c:Column {name: $column_name, type: $column_type})
            MERGE (t)-[:HAS_COLUMN]->(c)
        """, table=table, column_name=column_name, column_type=column_type)

def extract_metadata(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    metadata = {}
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        metadata[table_name] = columns
    
    conn.close()
    return metadata

def query_columns_of_table(neo4j_handler, table_name):
    query = """
    MATCH (t:Table {name: $table_name})-[:HAS_COLUMN]->(c:Column)
    RETURN c.name AS column_name, c.type AS column_type
    """
    with neo4j_handler.driver.session() as session:
        result = session.run(query, table_name=table_name)
        for record in result:
            print(f"Column: {record['column_name']}, Type: {record['column_type']}")

# Usage
db_path = 'banking_system.db'
metadata = extract_metadata(db_path)
uri=os.getenv('NEO4J_URI')
user=os.getenv('NEO4J_USER')
password=os.getenv('NEO4J_PASSWORD')
neo4j_handler = GraphDatabaseHandler(uri, user, password)
neo4j_handler.create_metadata_graph(metadata)

# Query columns of a specific table
query_columns_of_table(neo4j_handler, "Customer_Transaction_History")

# Close the Neo4j handler
neo4j_handler.close()