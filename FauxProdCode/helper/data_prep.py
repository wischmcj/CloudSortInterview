from pickle import FALSE
import pandas as pd
import os as os
import csv
 
from . import globals 

import os
import csv

##special processing for certain companies can be semented int of functions 
def process_jeffs_files


##itterates over a given directory to read in all the filed there 
 
with open('data.csv', 'w', encoding="utf8", newline='' ) as csvfile: 
  fieldnames = ['origin_Zip', 'destination_zip', 'package_id']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()

  path=globals.PATH            
  list_of_files = {}
  for filename in os.listdir(path):
     # if the element is an CSV file then...
     if filename[-4:] == ".csv":
         company_code = filename[-4:-4]
         list_of_files[filename] = path + "\\" + filename 
         print   (list_of_files[filename]) 
         with open(list_of_files[filename], encoding="utf8" ) as f:
            csv_f = csv.reader(f)
            for i, row in enumerate(csv_f):
               if i > 5 and len(row) > 1 :
                 print(row)
                 writer.writerow({'F1': row[0], 'F2': row[1]})