import pandas as pd

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)
df =pd.read_csv('C:/Users/user/PycharmProjects/pythonProject/Data/data/survey_results_public.csv')
#print(df.head(4))
#print(df.shape)
#print(df.info())
schema_df=pd.read_csv('C:/Users/user/PycharmProjects/pythonProject/Data/data/survey_results_schema.csv')
print(schema_df)
print("displying Hobbyist value")
print(df['Hobbyist'].value_counts())
print(df.loc[0:2,'Hobbyist':'Employment'])
