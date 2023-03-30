from pickle import FALSE
import pandas as pd
import os as os
import numpy as np
import networkx as nx
import csv

from pyvis.network import Network

from uszipcode import SearchEngine, SimpleZipcode, ComprehensiveZipcode


def write(df,file):
    f = open(file, 'w')
    df.to_csv(file, encoding='utf-8', index=False)
    
    f.close()

bie_pld1 = pd.read_csv("./cloudsort_bie_interview_pld1.csv", nrows=1000)

bie_pld1

#get statistical summary to guide grouping 
bie_pld1["Volume"] = bie_pld1["Length"]* bie_pld1["Width"]* bie_pld1[ "Height"]

#print("Display Volume Column")
#print(bie_pld1.head())

size_stats =bie_pld1[["Length", "Width", "Height", "Volume", "WeightOunces"]].describe()


 # limiting size to make data munging faster

#bie_pld1 = bie_pld1.head(10000) 

# enrich information and add grouping columns 

bie_pld1["orig_and_dest"] = str(bie_pld1["OriginZip"]) + str(bie_pld1["DestinationZip"])

def get_city(zip):
    try:
        search = SearchEngine()
        return search.by_zipcode(int(zip)).major_city
    except AttributeError:
        return "Not Found"

def get_state(zip):
    try:
        search = SearchEngine()
        return search.by_zipcode(int(zip)).state
    except AttributeError:
        return "Not Found"

bie_pld1["orig_city"]= bie_pld1["OriginZip"].apply(np.vectorize(get_city))
bie_pld1["dest_city"]= bie_pld1["DestinationZip"].apply(np.vectorize(get_city))
bie_pld1["orig_state"]= bie_pld1["OriginZip"].apply(np.vectorize(get_state))
bie_pld1["dest_state"]= bie_pld1["DestinationZip"].apply(np.vectorize(get_state))

#print("Display grouping columns")
print(bie_pld1.head())

# #group and summarize data
pld_summary = bie_pld1.groupby(["OriginZip", "DestinationZip"]).agg(
     num_orders = ('OrderCount','sum'), ##total number  of orders
     count_orders = ('OrderCount','count'),##total number of rows
     max_orders = ('OrderCount','max'),
     avg_volume = ('Volume','mean'),
     max_volume = ('Volume','max'),
     min_volume = ('Volume','min'),
     ).reset_index()

#print("Display summarized data")
print(pld_summary.head())     

pld_summary["orders_per_day"] = pld_summary["num_orders"]/30

write(pld_summary,'./cloudsort_bie_interview_summary.csv')


pld_summary_state = bie_pld1.groupby(["orig_state", "dest_state"]).agg(
     num_orders = ('OrderCount','sum'), ##total number  of orders
     count_orders = ('OrderCount','count'),##total number of rows
     max_orders = ('OrderCount','max'),
     avg_volume = ('Volume','mean'),
     max_volume = ('Volume','max'),
     min_volume = ('Volume','min'),
     ).reset_index()

print(pld_summary.head())  

pld_summary_state["orders_per_day"] = pld_summary_state["num_orders"]/30

write(pld_summary,'./cloudsort_bie_interview_summary_state.csv')


# pld_summary_by_cities = pd.DataFrame({'count' :bie_pld1.groupby(["orig_city", "dest_city"])["OrderCount"].size(),'sum' :bie_pld1.groupby(["OriginZip", "DestinationZip"])["OrderCount"].sum()}).reset_index()

# pld_summary_by_states = pd.DataFrame({'count' :bie_pld1.groupby(["orig_state", "dest_state"])["OrderCount"].size(),'sum' :bie_pld1.groupby(["OriginZip", "DestinationZip"])["OrderCount"].sum()}).reset_index()



# #print some summary values for investigation
# max_count = pld_summary["count"].idxmax()

# # print(max_count)
# # print(pld_summary_by_both["count"].mean())


# print('summary stats')
# print(pld_summary.head())
# print(pld_summary.count())
# #create network graph
# edgelist = pd.DataFrame({'source'  : pld_summary["OriginZip"],
#                                 'target'  : pld_summary["DestinationZip"],
#                                 'type'  : 'directed',
#                                 'weight'  : pld_summary["count"]
#                                   })
# print('edge stats')
# print (edgelist.count())
# print (edgelist.value_counts())
# G = nx.from_pandas_edgelist(edgelist,source="source",target = "target",edge_attr = "weight" )

# #get connectivity meaures 
# # returns a Dictionary with clustering value of each node
# print(nx.clustering(G))
 
# # This returns clustering value of specified node
# print(nx.clustering(G, 'C'))



# # # #vizualise the graph n pyvis
# # net= Network(notebook=True)
# # net.from_nx(G)
# # net.show("example.html")

# # node_list = list(set(edgelist['source'].unique().tolist() + \
# #                         edgelist['target'].unique().tolist()))
# # nodes =  pd.DataFrame({'id'  : node_name,  'label' : node_name, 'shape': 'dot', 'size': 5 }
# #                                for i,node_name in enumerate(node_list)
# #                                   )
# # edges = []
# # for row in edgelist.to_dict(orient='records'):
# #     source, target = row['source'], row['target']
# #     edges.append({
# #         'id': source + "__" + target,
# #         'from': source,
# #         'to': target,
# #         'width': 2,
# #     })

