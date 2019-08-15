import pandas as pd
import numpy as np

df = pd.read_csv("BoilerTags_July31_Validation.csv")
subset = pd.DataFrame(df)
isEmpty = pd.isnull(subset['invalid'])
validsub = subset[isEmpty]

validsub.to_csv("BoilerTags_July31_Taglist.csv")