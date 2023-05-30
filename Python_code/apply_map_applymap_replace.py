import pandas as pd

People={
    "first":["rahul","Sujeet","Saurabh"],
    "last":["ranjan","kumar","kumar"],
    "email":["r@gmail.com","s@gmail.com","K@gmail.com"]
}
#Updating multiple rows
#a.apply
#b.map
#c.applymap
#d.replace

df=pd.DataFrame(People)
length=df['email'].apply(len)
print('length of each email is \n', length)

def upper(email):
    return email.upper()

df['email']=df['email'].apply(upper)
print(df)
print(df.apply(len))

length_all_row=df.applymap(len)
print(length_all_row)
Updated_record={'rahul':'Niraj','Sujeet':'chintu'}
print(df)
# df['first']=df['first'].map(Updated_record)
# print(df)
df['first']=df['first'].replace(Updated_record)
print(df)