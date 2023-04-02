import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def draw_graph(reduced_matrix): 
    G = nx.from_pandas_adjacency(reduced_matrix)
    G.name = "Graph from pandas adjacency matrix"
    isolated_lessons = list(nx.isolates(G))
    G.remove_nodes_from(isolated_lessons)
    nx.draw(G, with_labels=True)
    print(isolated_lessons)
    plt.show()

