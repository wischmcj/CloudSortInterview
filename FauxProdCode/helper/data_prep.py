from pickle import FALSE
import pandas as pd
import os as os
import csv
 
from . import globals 

from . import settings

import os
import csv
import logging

##special processing for certain companies can be semented int of functions 
def proces_spec_company_files(company_code, df):
   if company_code == '0003':
     df["OriginZip"] = '33602' ## dealing with a conmpany that only 
                               ## sends from one zipcode and doesn't provide the correct file 

##iterates over a given directory to read in all the files there 
##Establish some heuristic for file naming- say file names are ddmmyyyy_CCCC.csv where cccc is some company code 
##indicating the format 
 
with open('data.csv', 'w', encoding="utf8", newline='' ) as csvfile: 
  path=settings.PATH            
  list_of_files = {}
  for filename in os.listdir(path):
     # only reading files with proper type 
     if filename[-4:] == ".csv":
         company_code = filename[-8:-4] ##lets say that the last 4 digits of the file name are a certain company
         list_of_files[filename] = path + "\\" + filename 
         _df = pd.read_csv(list_of_files[filename] )
         _df["file_name"] = filename
         proces_spec_company_files(company_code, _df)
         logging.log(f"{filename} processed")