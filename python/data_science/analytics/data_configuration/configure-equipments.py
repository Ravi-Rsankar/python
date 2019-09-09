import requests
import json
import pandas as pd
import numpy as np
#import config as cfg

#print(cfg.url)
cfg = "http://13.250.111.245/exactapi"
customerId = "5c4ed3c4fe02914642b4d5ba"
siteId = "5c4ed3dbfe02914642b4d5bb"
unitId = "5c4ed3f5fe02914642b4d5bc"

units = pd.read_csv("D:\work\exactspace\scripts\csv scripts\Renusagar_New_Meta_Unique.csv")
units = pd.DataFrame(units)

eqsub = units[['system' ,'systemName' ,'equipment','equipmentType', 'equipmentName', 'equipmentInstance']]

# print(type(eqsub.equipmentName.unique()))
equnique = eqsub.equipmentName.unique()

for eq in equnique:
    urli = cfg + '/equipment?filter={"where":{"unitsId": "' + unitId + '", "name": "'+eq+'"}}'
    # print(urli)
    equipments = requests.get(urli).json()

    if(equipments==[]):
        # ADD
        row=eqsub.loc[eqsub['equipmentName'] == eq]
        row=row.drop_duplicates()
        print(row)

        data = {"name": eq,
        "equipmentType": row["equipmentType"],
        "equipment": row["equipment"],
        "equipmentInstance": row["equipmentInstance"],
        "siteId": siteId,
        "unitsId": unitId,
        "customerId": customerId,
        "system": row["system"],
        "systemName": row["systemName"]
        }

        post_url = cfg + '/equipment'
        post_req = requests.post(post_url, data=data)
        print(post_req.content)
    else:
        # UPDATE
        row=eqsub.loc[eqsub['equipmentName'] == eq]
        row=row.drop_duplicates()
        update = cfg + '/equipment/update?where={"unitsId": "' + unitId + '", "name": "'+eq+'"}'
  
        data = {"name": eq,
        "equipmentType": row["equipmentType"],
        "equipment": row["equipment"],
        "equipmentInstance": row["equipmentInstance"],
        "id": equipments[0].get('id'),
        "siteId": siteId,
        "unitsId": unitId,
        "customerId": customerId,
        "system": row["system"],
        "systemName": row["systemName"]
        }
        update_req = requests.post(update, data=data)
