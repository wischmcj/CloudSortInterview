from pickle import FALSE
import pandas as pd
import os as os
import numpy as np
import networkx as nx
import csv

from pyvis.network import Network

from uszipcode import SearchEngine, SimpleZipcode, ComprehensiveZipcode


def create_standard_file(start,end,package_volume,origin_dest_type='zip'):
    ##Extract needed info from the file provided, put in needed format
    return

#create a graph model of the network represente by the orders provided
#weights determine the significance of results: distance, orders per month, travel time 
def create_network_graph(pld, weight_column):
    edgelist = pd.DataFrame({'source'  : df["origin"],
                                 'target'  : df["destination"],
                                 'type'  : 'directed',
                                 'weight'  : df[weight_column]
                                   })
    G = nx.from_pandas_edgelist(edgelist,source="source",target = "target",edge_attr = "weight" )

def basic_net_stats():    
     G_stats = pd.DataFrame(
            {"Eccentricity:" nx.eccentricity(G)
                "Diameter": nx.diameter(G),
                "Radius": nx.radius(G),
                "Preiphery": list(nx.periphery(G)),
                "Center": list(nx.center(G)),
                "degrees_in" = [d for n, d in G.in_degree()]
                "degrees_out" = [d for n, d in G.out_degree()]
                }

def find_most_connected_hubs(num_hubs )
    #Returs a subgraph of the most connected components 
    Gcc = sorted(nx.weakly_connected_components(G), key=len, reverse=True)
    G0 = G.subgraph(Gcc[0:num_hubs])

def draw_graph(G, pos):
    nx.draw_networkx_edges(G, pos = pos, edge_color="r", width=1.0, alpha=0.5, arrows = False)

def node_stats(G):    
    nnodes = G.number_of_nodes()
    degrees_in = [d for n, d in G.in_degree()]
    degrees_out = [d for n, d in G.out_degree()]
    avrg_degree_in = sum(degrees_in) / float(nnodes)
    avrg_degree_out = sum(degrees_out) / float(nnodes)

def map_graph(g):
  # USE PLt and basemap to draw on map of the us 