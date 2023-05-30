import pandas as pd
People={
    "first":["rahul","Sujeet","Saurabh"],
    "last":["ranjan","kumar","kumar"],
    "email":["r@gmail.com","s@gmail.com","K@gmail.com"]
}
DF1=pd.DataFrame(People)
print(DF1[['first','email']])
print(type(DF1['email']))
print(DF1.columns)
print(DF1.iloc[[0,1],2])
print(DF1.loc[[0,1],'email'])

