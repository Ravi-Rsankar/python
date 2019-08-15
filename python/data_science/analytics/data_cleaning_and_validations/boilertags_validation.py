import pandas as pd
import numpy as np

df = pd.read_csv("BoilerTags_July31_Cleaned.csv")
measureDF = pd.read_csv("BoilerTags_Approved_Measures.csv")
validsub2 = pd.DataFrame(df)
columns = ['dataTagId','description','system' ,'systemName' ,'equipment', 'equipmentName','equipmentInstance','measureType','measureInstance']

# Rule-1: These columns should neither be empty nor should they contain invalid arguments(???, ??)
validsub2['invalid'] = validsub2.apply(lambda row: ', '.join('Rule-1: '+i for i in columns if(row[i] =='???' or row[i] =='??' or pd.isnull(row[i]))), axis=1)

isEmpty=validsub2['invalid']==''
validsub = validsub2[isEmpty]

# Rule-2: For each equipmentName - Unique number of equipment and equipmentInstance should be 1
eqplist = validsub.equipmentName.unique()
for eqp in eqplist:           
    eqsub = validsub.loc[validsub.equipmentName==eqp,:]
#    eqList = eqsub.index[eqsub['equipmentName']==eqp].tolist()
    eqCount = eqsub.equipment.nunique()
    eqInCount = eqsub.equipmentInstance.nunique()
    
    if(eqCount !=1 or eqInCount !=1):
        validsub2.loc[eqsub.index, 'invalid'] = 'Rule-2: Equipment - equipmentInstance mismatch'
    else:
        # Rule-3: For each componentName - Unique number of component and componentInstance should be 1
        complist = eqsub.componentName.unique()
        for comp in complist: 
            if comp == "":
                continue
            compsub = eqsub.loc[eqsub.componentName==comp,:]
            cpCount = compsub.component.nunique()
            cpInCount = compsub.componentInstance.nunique()

            if(cpCount !=1 or cpInCount !=1):
                validsub2.loc[compsub.index,'invalid'] = 'Rule-3: Component - componentInstance mismatch'
        
        # Rule-4: For each subcomponentName - Unique number of subcomponent and subcomponentInstance should be 1
        subcomplist = eqsub.subcomponentName.unique()
        for subcom in subcomplist:
            sCompSub = eqsub.loc[eqsub.subcomponentName==subcom,:]
            scpCount = sCompSub.subcomponent.nunique()
            scpInCount = sCompSub.subcomponentInstance.nunique()
            if(scpCount !=1 or scpInCount !=1):
                validsub2.loc[sCompSub.index,'invalid'] = 'Rule-4: Subcomponent - SubcomponentInstance mismatch'

        # Rule-5: For each measureLocationName - Unique number of measureLocation and measureLocationInstance should be 1
        msrlist = eqsub.measureLocationName.unique()
        for msrcom in msrlist:
            msrsub = eqsub.loc[eqsub.measureLocationName==msrcom,:]
            msrCount = msrsub.measureLocation.nunique()
            msrInCount = msrsub.measureLocationInstance.nunique()
            if(msrCount !=1 or msrInCount !=1):
                validsub2.loc[msrsub.index,'invalid'] = 'Rule-5: MeasureLocation - MeasureInstance mismatch'
        
        # Rule-7: Check the measureType is in the approved list
        # Rule-8: For a measureType check if measureUnit is in the approved list.
#        mTypeUnique = measureDF.measureType.unique()
        mTypeList =measureDF['measureType'].tolist()
#        for mtype in eqsub.measureType.unique():
        for mtype in eqsub['measureType'].tolist():
            index=eqsub[eqsub['measureType']==mtype].index.tolist()[0] #Get the index of the row for a value in a column
            if(mtype not in mTypeList):
                validsub2.loc[index,'invalid'] = 'Rule-7'
            else:
                value = measureDF['measureType']==mtype
                mdf = measureDF[value]
                row = eqsub.loc[eqsub['measureType']==mtype]
                flag=~row['measureUnit'].isin(mdf['measureUnit'])
#                print(~row['measureUnit'].isin(mdf['measureUnit']))
#                exit()
                if(flag.any()):
                    validsub2.loc[index,'invalid'] = 'Rule-8: MeasureUnit - MeasureType mismatch'
                

# Rule-6: Duplicate taglist check - No two rows should have same values in the following columns                
globalcheck = ['system' ,'systemName' ,'equipment', 'equipmentType', 'equipmentName','equipmentInstance', 'component', 'componentName', 'componentInstance', 'subcomponent', 'subcomponentName', 'subcomponentInstance', 'measureLocation', 'measureLocationName', 'measureLocationInstance', 'measureProperty', 'measureType','measureInstance', 'measureUnit', 'tagType']

#Get the duplicates in the dataframe
duprow = validsub[validsub.duplicated(subset=globalcheck, keep=False)]

for row in duprow.index.tolist():
    validsub2.loc[row, 'invalid'] = 'Rule-6: Duplicate rows'

duptag = validsub[validsub.duplicated(subset='dataTagId', keep=False)]
for row in duptag.index.tolist():
    validsub2.loc[row, 'invalid'] = 'Rule-9: Duplicate dataTagId'


validsub2.to_csv("BoilerTags_July31_Validation.csv")
