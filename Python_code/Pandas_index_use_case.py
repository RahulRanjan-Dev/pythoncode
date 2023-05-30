import pandas as pd

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)
inputDf =pd.read_csv('C:/Users/user/PycharmProjects/pythonProject/Data/data/survey_results_public.csv',index_col='Respondent')
schemaDf=pd.read_csv('C:/Users/user/PycharmProjects/pythonProject/Data/data/survey_results_schema.csv',index_col='Column')
#print(inputDf)
schemaDf.sort_index(inplace=True)
print(schemaDf)
print(schemaDf.loc['Hobbyist','QuestionText'])