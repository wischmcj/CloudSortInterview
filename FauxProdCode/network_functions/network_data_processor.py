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
    print("Eccentricity: ", nx.eccentricity(G))
    print("Diameter: ", nx.diameter(G))
    print("Radius: ", nx.radius(G))
    print("Preiphery: ", list(nx.periphery(G)))
    print("Center: ", list(nx.center(G)))

def find_most_connected_hubs(num_hubs, )
    #


