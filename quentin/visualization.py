import networkx as nx
import output
import pandas as pd
import matplotlib.pyplot as plt

def draw_graph(reduced_matrix): 
    G = nx.from_pandas_adjacency(reduced_matrix)
    isolated_lessons = list(nx.isolates(G))
    nx.draw(G, with_labels=True)
    output.list(isolated_lessons)
    plt.show()

