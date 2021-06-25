#This script open latest file and extract tracenum, datetime, status
#parameter will be insert into trace table to generate new trace id for component table
#after generate new id, will get and insert value to teststep table
#by Raja Nazirul 23 July 2020
		
import glob
import os
import psycopg2
import json
import re
import os.path, time
from datetime import datetime
import types
        
class Insert_SQL:
    def __init__(self,filename):

        endtime = os.path.getmtime(filename)
        finishtime = datetime.fromtimestamp(endtime).strftime('%Y%m%d %H:%M:%S')

        try:
            # Filter parameter and take value from parameter
            param = [] #empty array

            # intermediate dictionary for traceability
            dict1 = {} #empty dict
            dict2 = []
            item = []

            # fields in the sample file 
            fields = ['traceability', 'starttime', 'status', 'finishtime', 'CRD', 'teststep', 'measresult', 'hilimit', 'lolimit', 'uom']
            keyword = ['MeasResult', 'pins', 'Overall']

            with open(filename) as fh: 
                for line in fh:
                    # read line by line from log file
                    description = list( line.strip().split(None, 8))
                
                    if 'Traceability' in description: 
                
                        param.append(description[3]) # param = [924048032002280029010001]
                        dict1[fields[0]]= param[0] # dict1 = { "traceability" : "924048032002280029010001"}

                    if 'DateTime' in description:

                        if '::' in description:
                            
                            param.append(finishtime)
                            dict1[fields[1]]= param[1]
                            
                        else:
                            param.append('{} {}'.format(description[2], description[3]))
                            dict1[fields[1]]= param[1]

                    if 'Overall_Status' in description:
                
                        param.append(description[2])
                        dict1[fields[2]]= param[2]

                    # intermediate dictionary for teststep
                    dict3 = {}
                    dict4 = {}
                    i = 0
                    j = 5
                    
                    if len(description) == 5 and keyword[0] not in description and keyword[1] not in description and keyword[2] not in description :  
                                                                                        
                        while i<len(description):
                            dict4[fields[j]] = description[i]
                            i = i + 1
                            j = j + 1
                                                   
                        dict2.append(dict4)

                param.append(finishtime)
                dict1[fields[3]]= param[3]
                dict1[fields[4]]= dict2
                item.append(dict1)
                
                # comment out to remove generate output file json
                out_file = open("test1.json", "a+")
                json.dump(item, out_file, indent=2)

                # remove comment to insert data to sql
                '''
                #connect database on postgreSQL
                conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=$ViTrox$")
                cur = conn.cursor()
                out_file = json.dumps(dict1, indent= 2)
                sql_query = """INSERT INTO test_json (json_data) VALUES (%s)"""
                cur.execute(sql_query, [out_file])
                conn.commit()'''

        except ValueError:
            pass

# comment out for infinite loop for continous running
#var = 1
#while var == 1:
try:
    list_of_files = glob.glob('C:/Users/rajan/Desktop/ICT_log_conversion/input_test_log/*') # * means all if need specific format then *.txt
    filename = min(list_of_files, key=os.path.getctime) # extract latest filename in folder
    Insert_SQL(filename) # call method to convert filename into json and insert into sql
    #os.remove(filename) # remove file after convert and go to the next latest file
    print('done') 
except ValueError:
    pass    