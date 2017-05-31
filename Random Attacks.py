# -*- coding: utf-8 -*-
"""
Created on Wed May 31 15:33:13 2017

@author: Qi Zhao (Homepage: zhaoqii.github.io)
"""
import numpy as np
import networkx as nx
import random as rd

# "adjacent" here is the adjacent matrix of China's high-speed railway network, and "city" is all citys' (stations')
# name, as noted in readme.md
degree = np.sum(adjacent, 1)  # compute the degree vector for every node
I = np.array(degree / np.sum(degree))  # I is the importance
entro = -np.sum(np.log(I) * I)       # network entropy based on node degree
         
graph = nx.from_numpy_matrix(adjacent)  # create NetworkX graph
#path = nx.all_pairs_shortest_path(graph, 100)   #compute all shortest paths
between = nx.betweenness_centrality(graph, normalized = True)   # compute all betweeness centrality
#between = nx.betweenness_centrality(graph, normalizedd = False)   # compute all betweeness centrality
between = np.array(pd.Series(between))
between = between[np.where(between != 0)]   # ensure the entropy is computable
entropy = -np.sum(np.log(between) * between) # network entropy based on node betweeness centrality

## random attacks test
ratio = np.array(range(10))/10   # ratio of cities to be attacked (or eliminated)
times = 50     # times to run for computing the average entropy given each ratio
entro_ratio = np.zeros(len(ratio))   # "entro_ratio" saves the average entropy given each ratio based on node degree
entropy_ratio = np.zeros(len(ratio))    # "entropy_ratio" saves the average entropy given each ratio based on betweenness centrality
for ii in range(len(ratio)):
    entro_new = np.zeros(times)
    entropy_new = np.zeros(times)
    for i in range(times):
        adjacent_new = adjacent.copy()
        target_no = rd.sample(list(range(citynum)), int(np.floor(citynum * ratio[ii]))) # randomly sample those cities to be attacked

        adjacent_new[target_no, :] = 0    # attack the cities we sampled
        adjacent_new[:, target_no] = 0
                    
        degree_new = np.sum(adjacent_new, 1)
        I_new = np.array(degree_new / np.sum(degree_new))
        I_new = I_new[np.where(I_new != 0)]
        entro_new[i] = -np.sum(np.log(I_new) * I_new)            
        #print('Entropy based on degree:', entro_new[i])
             
        graph_new = nx.from_numpy_matrix(adjacent_new)  # creat NetworkX graph
        between_new = nx.betweenness_centrality(graph_new, normalized = True)   # compute all betweeness centrality
        #between = nx.betweenness_centrality(graph, normalizedd = False)   # compute all betweeness centrality
        between_new = np.array(pd.Series(between_new))
        between_new = between_new[np.where(between_new != 0)]
        entropy_new[i] = -np.sum(np.log(between_new) * between_new)
        #print('Entropy based on betweenness centrality:', entropy_new[i])
        #print()
    entro_ratio[ii] = np.sum(entro_new)/times   # average node degree based entropy on each ratio
    entropy_ratio[ii] = np.sum(entropy_new)/times   # average betweenness centrality based entropy on each ratio
entro_pct = -(entro_ratio - entro) / entro       #  # compute the loss (percentage) of entropy from the initial entropy
entropy_pct = -(entropy_ratio - entropy) / entropy
