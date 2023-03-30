import requests
import math
from pickle import FALSE
import pandas as pd
import os as os
import numpy as np
import networkx as nx
import csv
from . import globals 

from uszipcode import SearchEngine, SimpleZipcode, ComprehensiveZipcode
import requests, json

api_key = globals.google_api_key
 
# Take source as input
source = input()
 
# Take destination as input
dest = input()
 
# url variable store url
url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
 
# Get method of requests module
# return response object
r = requests.get(url + 'origins = ' + source +
                   '&destinations = ' + dest +
                   '&key = ' + api_key)
                    
# json method of response object
# return json format result
x = r.json()

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
