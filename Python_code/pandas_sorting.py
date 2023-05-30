import pandas as pd

People={
    "first":["Gaurav","Aviansh","chintu"],
    "last":["ranjan","kumar","kumar"],
    "email":["g@gmail.com","s@gmail.com","c@gmail.com"]
}

df=pd.DataFrame(People)
df.sort_values(by=['first','last'],ascending=[True,False],inplace=True)
print(df)
df=df.sort_index()
print(df)