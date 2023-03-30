import requests
import math
from pickle import FALSE
import pandas as pd
import os as os
import numpy as np
import networkx as nx
import csv
 
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
print("There are about %f miles between zipcodes %s and %s"%(dist_miles,zip1,zip2))