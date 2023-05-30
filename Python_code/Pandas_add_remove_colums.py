import pandas as pd

People={
    "first":["rahul","Sujeet","Saurabh"],
    "last":["ranjan","kumar","kumar"],
    "email":["r@gmail.com","s@gmail.com","K@gmail.com"]
}


inputDf=pd.DataFrame(People)
#print(inputDf['first'] +" "+inputDf['last'])
inputDf['Full_name']=inputDf['first'] +" "+inputDf['last']
print(inputDf)
inputDf.drop(columns=['first','last'],inplace=True)
print(inputDf)
inputDf[['first','last']]=inputDf['Full_name'].str.split(' ',expand=True)
inputDf.drop(columns=['Full_name'],inplace=True)
print(inputDf)

# inputDf._append({"first":"Niru"},ignore_index=True)
# print(inputDf)

People2={
    "first":["Gaurav","Aviansh","chintu"],
    "last":["ranjan","kumar","kumar"],
    "email":["g@gmail.com","s@gmail.com","c@gmail.com"]
}

inputDf2=pd.DataFrame(People2)
inputDf=inputDf._append(inputDf2,ignore_index=True,sort=False)
print("New Appended DataFrame\n",inputDf)
inputDf.drop(index=5,inplace=True)
print(inputDf)

