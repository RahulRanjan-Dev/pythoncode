import pandas as pd

People={
    "first":["rahul","Sujeet","Saurabh"],
    "last":["ranjan","kumar","kumar"],
    "email":["r@gmail.com","s@gmail.com","K@gmail.com"]
}
df=pd.DataFrame(People)
print(df.columns)
df.columns=['first name', 'last name', 'email id']
df.columns=[ x.lower() for x in df.columns ]
df.columns=df.columns.str.replace(" ","_")
print(df)
#df.replace("Sujeet", "Dfirst",inplace=True)
df.rename(columns={"first_name":"first","last_name":"last"},inplace=True)
print(df)
df.loc[2]=["Niraj","kumar","Nir@gmail.com"]
df.loc[2,["first","last"]]=["Saurabh","kumar"]
print(df)
#df['email_id'].replace("r@gmail.com","rr@gmail.com",inplace=True)
fil_cond=(df['email_id']=='r@gmail.com')
df.loc[fil_cond,'email_id']='ranjan@gmail.com'
print(df)
df['email_id']=df['email_id'].str.upper()
print(df)





