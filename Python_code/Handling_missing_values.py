import numpy as np
import pandas as pd

People={
    "first":["Gaurav","Aviansh","chintu",np.nan,np.nan],
    "last":["ranjan","kumar","kumar",np.nan,"Nir"],
    "email":["g@gmail.com","s@gmail.com","c@gmail.com",np.nan,np.nan],
    "Age":["23","45","45","78","89"]
    }
df=pd.DataFrame(People)
print(df)
df=df.dropna(axis='index',how='all')
print(df)
print(df.isna())
df=df.fillna("AC")
print(df.dtypes)
df["Age"]=df["Age"].astype(float)
print(df.dtypes)
na_vals=['NA','Missing']
inputDf =pd.read_csv('C:/Users/user/PycharmProjects/pythonProject/Data/data/survey_results_public.csv',na_values=na_vals)
inputDf['YearsCode'].unique()