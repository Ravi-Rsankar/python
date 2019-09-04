import requests
import json
import pandas as pd
#import config as cfg
import numpy as np 

cfg = "http://13.250.111.245/exactapi"
customerId = "5c4ed3c4fe02914642b4d5ba"
siteId = "5c4ed3dbfe02914642b4d5bb"
unitId = "5c4ed3f5fe02914642b4d5bc"

units = pd.read_csv("D:\work\exactspace\scripts\csv scripts\Renusagar_New_Meta_Unique.csv")
units = pd.DataFrame(units)

dataTags = units.dataTagId
# print(dataTags)
for i in range(0, units.shape[0]):
    urli = cfg +'/tagmeta/?filter={"where":{"dataTagId":"'+units.loc[i,'dataTagId']+'"}}'
    rows = requests.get(urli)
    if(rows.status_code == 200):
        rows = json.loads(rows.content)
        csv_row = units.loc[i]
        equipmentName = units.loc[i,'equipmentName']
        # print("--eq ", equipmentName)
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
        
        if(rows==[] or rows[0].get('equipmentName') != units.loc[i,'equipmentName']):
            # ADD
            eq_url = cfg + '/equipment?filter={"where":{"unitsId": "' + unitId + '", "name": "'+units.loc[i,'equipmentName']+'"}}'
            eq_json = requests.get(eq_url)
            if(eq_json.status_code == 200):
                eq_json = json.loads(eq_json.content)
                eq_Id=eq_json[0].get('id')
                data['equipmentId'] = eq_Id
                print(eq_Id)
                post_url = cfg + '/equipment/'+eq_Id+'/tagmeta'
                post_req = requests.post(post_url, data=data)
                print(post_req.content)
      
        elif(rows[0].get('equipmentName') == units.loc[i,'equipmentName']):
            data["equipmentId"] = rows[0].get('equipmentId')
            # print(data)
            update_url = cfg + '/tagmeta/update?where={"dataTagId" : "' +rows[0].get('dataTagId')+'"}'
            update_req = requests.post(update_url, json=data)
            print(update_req.content)
