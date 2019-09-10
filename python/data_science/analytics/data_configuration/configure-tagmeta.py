import requests
import json
import pandas as pd
#import config as cfg
import numpy as np 

# has to be moved to the config file
cfg = "http://13.250.111.245/exactapi"
customerId = "5c4ed3c4fe02914642b4d5ba"
siteId = "5c4ed3dbfe02914642b4d5bb"
unitId = "5c4ed3f5fe02914642b4d5bc"

units = pd.read_csv("D:\work\exactspace\scripts\csv scripts\Renusagar_New_Meta_Unique.csv")
units = pd.DataFrame(units)

# print(dataTags)
for i in range(0, units.shape[0]):
    urli = cfg +'/tagmeta/?filter={"where":{"dataTagId":"'+units.loc[i,'dataTagId']+'"}}'
    db_rows = requests.get(urli)
    if(db_rows.status_code == 200):
        # print(db_rows.content)
        db_rows = json.loads(db_rows.content)
        csv_row = units.loc[i]
        # print(units.loc[i,'dataTagId'])
        # equipmentName = units.loc[i,'equipmentName']
        data = {
        "equipmentName": units.loc[i,'equipmentName'],
        "equipment": units.loc[i,'equipment'],
        "equipmentType": units.loc[i,'equipmentType'],
        "equipmentInstance": units.loc[i,'equipmentInstance'],
        "component": units.loc[i,'component'],
        "componentInstance": units.loc[i,'componentInstance'],
        "subcomponent": units.loc[i,'subcomponent'],
        "subcomponentInstance": units.loc[i,'subcomponentInstance'],
        "measureProperty": units.loc[i,'measureProperty'],
        "measureType": units.loc[i,'measureType'],
        "measureInstance": units.loc[i,'measureInstance'],
        "measureUnit": units.loc[i,'measureUnit'],
        "lcl": units.loc[i,'lcl'],
        "ucl": units.loc[i,'ucl'],
        "description": units.loc[i,'description'],
        "dataTagId": units.loc[i,'dataTagId'],
        "componentName": units.loc[i,'componentName'],
        "standardDescription": units.loc[i,'standardDescription'],
        "system": units.loc[i,'system'],
        "tagType": units.loc[i,'tagType'],
        "group": units.loc[i,'group'],
        "designValue": units.loc[i,'designValue'],
        "goodDirection": units.loc[i,'goodDirection'],
        "systemName": units.loc[i,'systemName'],
        "unitsId": unitId
        }

        if(len(db_rows) > 1):
            print()
            # print('--> ',db_rows)
            # print(db_rows['equipmentName'])
            eqn_list=[]
            for m in range(0,len(db_rows)):
                eqn_list.append(db_rows[m].get('equipmentName'))
            print(eqn_list)
            for n in range(0,len(db_rows)):
                if(db_rows[n].get('equipmentName') == units.loc[i,'equipmentName']):
                    # update
                    data["equipmentId"] = db_rows[n].get('equipmentId')
                    update_url = cfg + '/tagmeta/update?where={"dataTagId" : "' +db_rows[n].get('dataTagId')+'"}'
                    # print('update--- ',data)
                    print()
                    # update_req = requests.post(update_url, data=data)

                else:
                    # Add
                    eq_url = cfg + '/equipment?filter={"where":{"unitsId": "' + unitId + '", "name": "'+units.loc[i,'equipmentName']+'"}}'
                    eq_json = requests.get(eq_url)
                    if(eq_json.status_code == 200):
                        eq_json = json.loads(eq_json.content)
                        eq_Id=eq_json[0].get('id')
                        data['equipmentId'] = eq_Id
                        post_url = cfg + '/equipment/'+eq_Id+'/tagmeta'
                        # print('add -- ',data)
                        # post_req = requests.post(post_url, data=data)
        
        # print(i)
        # CASE-3: If tag doesn't exist [if db_rows == []]
        if(db_rows==[]):
            # Add
            eq_url = cfg + '/equipment?filter={"where":{"unitsId": "' + unitId + '", "name": "'+units.loc[i,'equipmentName']+'"}}'
            eq_json = requests.get(eq_url)
            if(eq_json.status_code == 200):
                eq_json = json.loads(eq_json.content)
                eq_Id=eq_json[0].get('id')
                data['equipmentId'] = eq_Id
                post_url = cfg + '/equipment/'+eq_Id+'/tagmeta'
                post_req = requests.post(post_url, data=data)
        
        # elif(len(db_rows)>1):
        #     for i in range(0,len(db_rows)):
        #         print(db_rows[i].get('equipmentName'))

        # Case 2: If equipmentName in csv and db did not match. then fetch the eqid from the db
        elif( db_rows[0].get('equipmentName') != units.loc[i,'equipmentName']):
            # Update the equipment ID
            eq_url = cfg + '/equipment?filter={"where":{"unitsId": "' + unitId + '", "name": "'+units.loc[i,'equipmentName']+'"}}'
            eq_json = requests.get(eq_url)
            
            if(eq_json.status_code == 200):
                eq_json = json.loads(eq_json.content)
                eq_Id=eq_json[0].get('id')
                data['equipmentId'] = eq_Id
                update_url = cfg + '/tagmeta/update?where={"dataTagId" : "' +db_rows[0].get('dataTagId')+'"}'
                update_req = requests.post(update_url, data=data)
        
        # Case 1: If equipmentName in csv and db matches then update the row in db      
        else:                  
            # Update the row with latest values    
            data["equipmentId"] = db_rows[0].get('equipmentId')
            update_url = cfg + '/tagmeta/update?where={"dataTagId" : "' +db_rows[0].get('dataTagId')+'"}'
            update_req = requests.post(update_url, data=data)
