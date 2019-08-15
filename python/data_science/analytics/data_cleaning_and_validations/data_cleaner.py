import pandas as pd
import numpy as np

df = pd.ExcelFile("0-Meta List- Aug12.xlsx")
# Read the sheet in the excel
bt=df.parse('Boiler Tags')
cleansub = pd.DataFrame(bt)
spaceCheck = ['description','system' ,'systemName' ,'equipment', 'equipmentName','component','componentName','subcomponent', 'subcomponentName', 'measureLocation', 'measureLocationName', 'measureProperty', 'measureType', 'measureUnit', 'tagType', 'group']

caseCheck = ['system', 'equipment', 'component','componentName','subcomponent', 'subcomponentName', 'measureLocation', 'measureLocationName', 'measureProperty', 'measureType', 'group']

# Strip, remove double spaces and ? in the data
for col in spaceCheck:

    cleansub[col]=cleansub[col].str.strip()
    cleansub[col]=cleansub[col].str.replace('\s+',' ')
    cleansub[col]=cleansub[col].str.replace('\?','')

# Ensure title case in the data. There are certain wildcards which are handled outside the loop
for col in caseCheck:
    
    cleansub[col]= cleansub[col].str.title() 

    cleansub[col] = cleansub[col].str.replace('Ce ', 'CE ')
    cleansub[col] = cleansub[col].str.replace('Ee ', 'EE ')
    cleansub[col] = cleansub[col].str.replace('Gd ', 'GD ')

    cleansub[col] = cleansub[col].str.replace('Aph', 'APH')
    cleansub[col] = cleansub[col].str.replace('Cw ', 'CW ')
    cleansub[col] = cleansub[col].str.replace('Esp', 'ESP')
    cleansub[col] = cleansub[col].str.replace('Fd ', 'FD ')
    cleansub[col] = cleansub[col].str.replace('Sh ', 'SH ')
    cleansub[col] = cleansub[col].str.replace('Id ', 'ID ')
    cleansub[col] = cleansub[col].str.replace('Pa ', 'PA ')
    cleansub[col] = cleansub[col].str.replace('Rh ', 'RH ')

    cleansub[col] = cleansub[col].str.replace('Bcw', 'BCW')
    cleansub[col] = cleansub[col].str.replace('Sadc', 'SADC')
    cleansub[col] = cleansub[col].str.replace('Vfd', 'VFD')
    cleansub[col] = cleansub[col].str.replace('Lo ', 'LO ')

    cleansub[col] = cleansub[col].str.replace('Bcwp', 'BCWP')
    cleansub[col] = cleansub[col].str.replace('Fdr', 'FDR')
    cleansub[col] = cleansub[col].str.replace('Ab', 'AB')
    cleansub[col] = cleansub[col].str.replace('Bc', 'BC')
    cleansub[col] = cleansub[col].str.replace('Cd', 'CD')
    cleansub[col] = cleansub[col].str.replace('De', 'DE')
    cleansub[col] = cleansub[col].str.replace('Ef', 'EF')
    cleansub[col] = cleansub[col].str.replace('Fg', 'FG')
    cleansub[col] = cleansub[col].str.replace('Gg', 'GG')
    
    cleansub[col] = cleansub[col].str.replace('Cbd', 'CBD')
    cleansub[col] = cleansub[col].str.replace('Sa ', 'SA ')
    cleansub[col] = cleansub[col].str.replace('Ch-', 'CH-')
    cleansub[col] = cleansub[col].str.replace('Sd', 'SD')
    cleansub[col] = cleansub[col].str.replace('Nde', 'NDE')
    cleansub[col] = cleansub[col].str.replace('Hfo', 'HFO')
    cleansub[col] = cleansub[col].str.replace('Lofa', 'LOFA')
    cleansub[col] = cleansub[col].str.replace('Uofa', 'UOFA')
    cleansub[col] = cleansub[col].str.replace('Hrh', 'HRH')
    cleansub[col] = cleansub[col].str.replace('Crh', 'CRH')
    cleansub[col] = cleansub[col].str.replace('Sb', 'SB')
    cleansub[col] = cleansub[col].str.replace('Gb', 'GB')
 
    cleansub[col]=cleansub[col].str.strip()

cleansub['measureType'] = cleansub['measureType'].str.replace('Sox', 'SOX')
cleansub['measureType'] = cleansub['measureType'].str.replace('Nox', 'NOX')
cleansub['measureType'] = cleansub['measureType'].str.replace('Ph', 'pH')
cleansub['measureType'] = cleansub['measureType'].str.replace(r'Co$', 'CO')

cleansub.to_csv("BoilerTags_July31_Cleaned.csv")