# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:36:05 2017

@author: Qi Zhao (Homepage: zhaoqii.github.io)
"""
from matplotlib import style
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

style.use('ggplot')

def show_graph(adjacency_matrix):    # visulize our network (Based on Scott's answer on Stackoverflow)

    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    nx.draw_networkx(gr)
    plt.show() 


# the following function is for showing the structure entropy values
# therefore, for checking the entropy values after attacking those specific cities, plz run
# graph_entropy(range(len(target)), entro_new, entropy_new) , after running the “Specific Attacks.py”;
# for checking the entropy values after random attacks, plz just run
# graph_entropy(ratio, entro_ratio, entropy_ratio) after running the “Random Attacks.py”
def graph_entropy(x, entro_ratio, entropy_ratio):
    plt.figure(1)
    plt.plot(x, entro_ratio, '-*', label = 'Entropy based on degree')
    plt.plot(x, entropy_ratio, label = 'Entropy based on betweeness centrality')
    plt.ylabel = 'Entropy'
    plt.xlabel = 'Ratio'
    plt.ylim(0,7)
    plt.legend()
    plt.show()



# the following function is for showing the loss (percentage) of entropy from the initial entropy
# therefore, for checking the loss of entropy after running “Specific Attacks.py”, run
# graph_entropy_pct(range(len(target)), entro_pct, entropy_pct, ylimdown = -0.02, ylimup = 0.05)
# for checking the loss of entropy after running “Random Attacks.py”, run
# graph_entropy_pct(ratio, entro_pct, entropy_pct, ylimdown = 0, ylimup = 1)
def graph_entropy_pct(x, entro_pct, entropy_pct, ylimdown = 0, ylimup = 1):
    plt.figure(1)
    plt.plot(x, entro_pct, '-*', label = 'Entropy loss based on degree')
    plt.plot(x, entropy_pct, label = 'Entropy loss based on betweeness centrality')
    plt.ylabel = 'Entropy Loss (%)'
    plt.xlabel = 'Ratio'
    plt.ylim(ylimdown, ylimup)
    plt.legend()
    plt.show()


