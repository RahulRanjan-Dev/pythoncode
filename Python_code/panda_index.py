import pandas as pd

People={
    "first":["rahul","Sujeet","Saurabh"],
    "last":["ranjan","kumar","kumar"],
    "email":["r@gmail.com","s@gmail.com","K@gmail.com"]
}
df=pd.DataFrame(People)
df.set_index('email',inplace=True)
print(df.index)
print(df.loc['r@gmail.com'])
print(df['first'])
df.reset_index(inplace=True)
print(df)