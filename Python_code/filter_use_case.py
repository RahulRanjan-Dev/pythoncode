import pandas as pd

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)
inputDf =pd.read_csv('C:/Users/user/PycharmProjects/pythonProject/Data/data/survey_results_public.csv',index_col='Respondent')
schemaDf=pd.read_csv('C:/Users/user/PycharmProjects/pythonProject/Data/data/survey_results_schema.csv',index_col='Column')
#print(inputDf)
countries=['United Kingdom','United States','Thailand','Ukraine']
fil_cond=inputDf['Country'].isin(countries)
cond=inputDf['LanguageWorkedWith'].str.contains('Python',na=False)
print(cond)
print(inputDf.loc[cond,'LanguageWorkedWith'])
print(inputDf.loc[cond,'Country'])