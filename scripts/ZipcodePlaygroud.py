
# from pickle import FALSE
# import pandas as pd
# import os as os

# import networkx as nx

# from pyvis.network import Network

# from uszipcode import SearchEngine, SimpleZipcode, ComprehensiveZipcode
# #zipcode functions 
# search = SearchEngine()
# zipcode = search.by_zipcode(34003)
# #zipcode.major_city
# zipcode.state_abbr
# # zipcode.population

# from pickle import FALSE
# import pandas as pd
# import os as os
# import numpy as np
# import networkx as nx

# from pyvis.network import Network

# from uszipcode import SearchEngine, SimpleZipcode, ComprehensiveZipcode
# #zipcode functions 

# #search = SearchEngine()
# #zipcode = search.by_zipcode(12409)
# #print(zipcode.major_city)
# # zipcode.state_abbr
# # zipcode.population

# # #sample zipcode grouping
# # zcdb = ZipCodeDatabase()
# # [z.zip for z in zcdb.get_zipcodes_around_radius('54901', 10)]

# bie_pld1 = pd.read_csv("./cloudsort_bie_interview_pld1.csv")
# bie_pld1 = bie_pld1.head(100)

# # enrich information and add grouping columns 

# #bie_pld1["orig_and_dest"] = str(bie_pld1["OriginZip"]) + str(bie_pld1["DestinationZip"])
# def get_city(zip):
#     search = SearchEngine()
#     return search.by_zipcode(int(zip)).major_city
# def get_state(zip):
#     search = SearchEngine()
#     return search.by_zipcode(int(zip)).state

# bie_pld1["orig_city"]= bie_pld1["OriginZip"].apply(np.vectorize(get_city))
# bie_pld1["dest_city"]= bie_pld1["DestinationZip"].apply(np.vectorize(get_city))
# bie_pld1["orig_state"]= bie_pld1["OriginZip"].apply(np.vectorize(get_state))
# bie_pld1["dest_state"]= bie_pld1["DestinationZip"].apply(np.vectorize(get_state))

# print(bie_pld1.head())



import requests
import math
 
def get_lat_lon(zip):
    uri = 'https://public.opendatasoft.com/api/records/1.0/search/?q={zip}&dataset=us-zip-code-latitude-and-longitude'
    return requests.get(uri.format(zip=zip)).json()["records"][0]['fields']['geopoint']

def rad(x):
  return x * math.pi / 180.0;


def getHaversineDistance(p1, p2):
  R = 6378137; # Earth’s mean radius in meter
  dLat = rad(p2[0] - p1[0]);
  dLong = rad(p2[1] - p1[1]);
  a = (math.sin(dLat / 2) * math.sin(dLat / 2) +
    math.cos(rad(p1[0])) * math.cos(rad(p2[0])) *
    math.sin(dLong / 2) * math.sin(dLong / 2))
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
  d = R * c #
  return d # // returns the distance in meter
def Meters2Miles(meters):
    return meters * 0.000621371

zip1 = input("Enter Zip1")
p1 = get_lat_lon(zip1)
zip2 = input("Enter Zip2")
p2 = get_lat_lon(zip2)
dist_meters = getHaversineDistance(p1,p2)
dist_miles = Meters2Miles(dist_meters)
print("There are about %f miles between zipcodes %s and %s"%(dist_miles,zip1,zip2))441