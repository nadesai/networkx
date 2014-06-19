#-*- coding: utf-8 -*-
#    Copyright (C) 2011 by 
#    Conrad Lee <conradlee@gmail.com>
#    Aric Hagberg <hagberg@lanl.gov>
#    All rights reserved.
#    BSD license.

import networkx as nx
from networkx.algorithms.connectivity import local_edge_connectivity

__author__ = """\n""".join(['Nikhil Desai (nikhilarundesai@gmail.com)'])
__all__ = ['girvan_newman_splits']

def girvan_newman_splits(G):
    g = G.copy()
    splits = []
    while G.number_of_edges() > 0:
        ebw = nx.edge_betweenness(G)
        max_edge = max(ebw, key=ebw.get)
        G.remove_edge(*max_edge)
        if in_same_connected_component(G, *max_edge): 
            splits.append(max_edge)
    return splits

def in_same_connected_component(G, u, v):
    return local_edge_connectivity(G, u, v) > 0
