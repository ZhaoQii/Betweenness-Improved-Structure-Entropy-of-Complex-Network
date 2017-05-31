# -*- coding: utf-8 -*-
"""
Created on Wed May 31 14:25:13 2017

@author: Qi Zhao (Homepage: zhaoqii.github.io)
"""
import numpy as np
import networkx as nx
import pandas as pd

# "adjacent" here is the adjacent matrix of China's high-speed railway network, and "city" is all citys' (stations')
# name, as noted in readme.md. Make sure run that code before running the below
degree = np.sum(adjacent, 1)  # compute the degree vector for every node
I = np.array(degree / np.sum(degree))  # I is the degree of importance
entro = -np.sum(np.log(I) * I)       # initial network entropy based on node degree
         
graph = nx.from_numpy_matrix(adjacent)  # create NetworkX graph
#path = nx.all_pairs_shortest_path(graph, 100)   #compute all shortest paths
between = nx.betweenness_centrality(graph, normalized = True)   # compute all betweeness centrality
#between = nx.betweenness_centrality(graph, normalizedd = False)   # compute all betweeness centrality
between = np.array(pd.Series(between))
between = between[np.where(between != 0)]   # ensure the entropy is computable
entropy = -np.sum(np.log(between) * between) # initial network entropy based on node betweeness centrality

## Specific attacks test
target = ['广州', '北京', '成都', '常州', '上海', '徐州', '石家庄', '郑州', '重庆', '杭州', '长沙', '西安']
   # target here contains several important cities in China, and we attack (deactivate or eliminate) them one by one 
   # and compute the structure entropy respectively
target_no = [city[city == x].index.tolist()[0] for x in target]  # get the correspondent sequence numbers for these cities
adjacent_new = adjacent.copy()
entro_new = np.zeros(len(target))   # "entro_new" saves the entropies based on node degree after specific attacks
entropy_new = np.zeros(len(target))     # "entropy_new" saves the entropies based on betweenness centrality after specific attacks
j = 0
for item in target_no:

    adjacent_new[item, :] = 0  # deactivate the target cities
    adjacent_new[:, item] = 0
                
    degree_new = np.sum(adjacent_new, 1)
    
    I_new = np.array(degree_new / np.sum(degree_new))
    I_new = I_new[np.where(I_new != 0)]
    entro_new[j] = -np.sum(np.log(I_new) * I_new)            
    print('Entropy based on degree:', entro_new[j])
         
    graph_new = nx.from_numpy_matrix(adjacent_new)  # creat NetworkX graph
    between_new = nx.betweenness_centrality(graph_new, normalized = True)   # compute all betweeness centrality
    #between = nx.betweenness_centrality(graph, normalizedd = False)   # compute all betweeness centrality
    between_new = np.array(pd.Series(between_new))
    between_new = between_new[np.where(between_new != 0)]
    entropy_new[j] = -np.sum(np.log(between_new) * between_new)
    print('Entropy based on betweenness centrality:', entropy_new[j])
    print()
    j += 1
entro_pct = -(entro_new - entro) / entro   # compute the loss (percentage) of entropy from the initial entropy
entropy_pct = -(entropy_new - entropy) / entropy
