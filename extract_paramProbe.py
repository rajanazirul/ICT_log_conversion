#This script open latest file and extract tracenum, datetime, status
#parameter will be insert into trace table to generate new trace id for component table
#after generate new id, will get and insert value to teststep table
#by Raja Nazirul 23 July 2020

import glob
import os
import psycopg2
import json

#Check latest update file in folder
list_of_files = glob.glob('C:/Users/rajan/Desktop/ICT_log_conversion/input_probe_log/probe_report.txt') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

fields = ['failure_type', 'probe', 'usage', 'node_name', 'datetime', 'device_name']
dict1 = {}
param = []
item = []
mc_id = '1'

print(latest_file)
#connect database on postgreSQL
#conn = psycopg2.connect("host=192.168.1.192 dbname=postgres user=postgres password=$ViTrox$")

#cur = conn.cursor()

#Filter parameter and take value from parameter
with open(latest_file) as fh:
    for line in fh:

        #read line by line from log file
        description = list( line.replace('|','').strip().split(None, 8))
        
        try:
            if len(description) < 7:
                
                param = [description[0],description[2],description[3],description[4],description[5]]
                param.append(mc_id)
                dict1[fields[0]] = param[0]
                dict1[fields[1]] = param[1]
                dict1[fields[2]] = param[2]
                dict1[fields[3]] = param[3]
                dict1[fields[4]] = param[4]
                dict1[fields[5]] = param[5]
                print(param)
                out_file = open("probe1.json", "a+")
                json.dump(dict1, out_file, indent=2)
                #cur.execute("INSERT INTO probe (failure_type, probe, usage, node_name, datetime, device_name) VALUES (%s, %s, %s, %s, %s, %s )", param)

            else:
                if 'type' not in description:
                    param = [description[0],description[2],description[3],description[4],description[5],description[6]]
                    dict1[fields[0]] = param[0]
                    dict1[fields[1]] = param[1]
                    dict1[fields[2]] = param[2]
                    dict1[fields[3]] = param[3]
                    dict1[fields[5]] = param[4]
                    dict1[fields[4]] = param[5]
                    print(param)
                    out_file = open("probe1.json", "a+")
                    json.dump(dict1, out_file, indent=2)
                    #cur.execute("INSERT INTO probe (failure_type, probe, usage, node_name, device_name, datetime) VALUES (%s, %s, %s, %s, %s, %s )", param)
            
        except IndexError:
            pass
            
#conn.commit()







        