import pandas as pd
import numpy as np

df = pd.read_csv("D:\work\exactspace\scripts\csv scripts\Renusagar_New_Meta.csv")
validsub2 = pd.DataFrame(df)

# Replace all nan with -
validsub2 = validsub2.fillna('-')

duptag = validsub2[validsub2.duplicated(subset='dataTagId', keep='first')]
for row in duptag.index.tolist():
    validsub2.loc[row, 'invalid'] = 'Rule-9: Duplicate dataTagId'


validsub2.to_csv("D:\work\exactspace\scripts\csv scripts\Renusagar_New_Meta_Unique.csv")
