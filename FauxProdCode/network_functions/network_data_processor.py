from pickle import FALSE
import pandas as pd
import os as os
import numpy as np
import networkx as nx
import csv


import basemap
import matplotlib.pyplot as plt
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

def basic_net_stats(G):    
    G_stats = pd.DataFrame(
            {"Eccentricity:" nx.eccentricity(G)
                "Diameter": nx.diameter(G),
                "Radius": nx.radius(G),
                "Preiphery": list(nx.periphery(G)),
                "Center": list(nx.center(G)),
                "degrees_in" = [d for n, d in G.in_degree()]
                "degrees_out" = [d for n, d in G.out_degree()]
                }
def find_most_connected_hubs(num_hubs, )
    Gcc = sorted(nx.strongly_connected_components(G), key=len, reverse=True)

def map_graph(g):
    plt.figure(figsize = (12,8))
    m = Basemap(projection='merc',llcrnrlon=-160,llcrnrlat=15,urcrnrlon=-60,
    urcrnrlat=50, lat_ts=0, resolution='l',suppress_ticks=True)
    mx, my = m(pos_data['lon'].values, pos_data['lat'].values)
    pos = {}
    for count, elem in enumerate(pos_data['nodes']):
        pos[elem] = (mx[count], my[count])
    nx.draw_networkx_edges(G, pos = pos, edge_color='blue', alpha=0.1, arrows = False)
    m.drawcountries(linewidth = 2)
    m.drawstates(linewidth = 0.2)
    m.drawcoastlines(linewidth=2)
    plt.tight_layout()
    plt.savefig("map.png", dpi = 300)
    plt.show()


