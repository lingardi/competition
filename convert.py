import pandas as pd
import numpy as np
def convertRate(row):
    if pd.isnull(row):
        return 1.0
    elif ':' in str(row):
        rows = row.split(':')
        return 1.0 - float(rows[1])/float(rows[0])
    else:
        return float(row)

df_off = pd.read_csv("D:\competition\ccf_offline_stage1_train.csv")
df_off['discount_rate'] = df_off['Discount_rate'].apply(convertRate)

print(df_off['discount_rate'].unique())
#df_off.apply(convertRate())

