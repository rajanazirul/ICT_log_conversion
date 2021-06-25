#This script open latest file and extract tracenum, datetime, status
#parameter will be insert into trace table to generate new trace id for component table
#after generate new id, will get and insert value to teststep table
#by Raja Nazirul 23 July 2020

import glob
import os
import psycopg2
import json

#Check latest update file in folder
list_of_files = glob.glob('C:/Users/rajan/Desktop/ICT_log_conversion/input_dgn_log/DGN.log') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

fields = ['test', 'subtest', 'module', 'slot', 'status', 'mc_id']
dict1 = {}
param = []
item = []
mc_id = '1'

print(latest_file)
#connect database on postgreSQL
#conn = psycopg2.connect("host=localhost dbname=ict_demo user=postgres password=$ViTrox$")

#cur = conn.cursor()

#Filter parameter and take value from parameter
with open(latest_file) as fh:
    for line in fh:

        #read line by line from log file
        description = list( line.replace(',','').strip().split(None, 8))

        #print(description)   
        if 'FAILED.' in description:
            
            param = [description[1],description[3],description[5],description[7],description[8]]
            param.append(mc_id)
            dict1[fields[0]] = param[0]
            dict1[fields[1]] = param[1]
            dict1[fields[2]] = param[2]
            dict1[fields[3]] = param[3]
            dict1[fields[4]] = param[4]
            dict1[fields[5]] = param[5]
            #item.append(dict1)

            print(param)
            #comment out to disable file output
            out_file = open("dgn1.json", "a+")
            json.dump(dict1, out_file, indent=2)

            #cur.execute("INSERT INTO dgn (test, subtest, module, slot, status, mc_id) VALUES (%s, %s, %s, %s, %s, %s )", param)

#conn.commit()








        