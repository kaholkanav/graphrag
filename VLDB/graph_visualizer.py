from py2neo import Graph
import networkx as nx
import matplotlib.pyplot as plt

# Connect to Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

# Run a query
data = graph.run("MATCH (n)-[r]->(m) RETURN n, r, m").data()

# Convert to NetworkX graph
G = nx.DiGraph()
for record in data:
    G.add_edge(record['n']['name'], record['m']['name'])

# Plot
nx.draw(G, with_labels=True)
plt.show()