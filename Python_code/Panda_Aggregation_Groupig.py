import pandas as pd

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)
inputDf =pd.read_csv('C:/Users/user/PycharmProjects/pythonProject/Data/data/survey_results_public.csv')

schema_df=pd.read_csv('C:/Users/user/PycharmProjects/pythonProject/Data/data/survey_results_schema.csv')
#print(schema_df)
fileDf=inputDf['ConvertedComp'].head(15)
print(inputDf['ConvertedComp'].median())
#print(inputDf.describe())
print(inputDf['Hobbyist'].value_counts())
print(inputDf['SocialMedia'].value_counts())
country_grp=inputDf.groupby(['Country'])
print("county group India")
#print(country_grp.get_group('India'))
print(country_grp['SocialMedia'].value_counts().loc['India'])
print(country_grp['ConvertedComp'].agg(['median','mean']))
seriesGropupobject=country_grp['LanguageWorkedWith'].apply(lambda x : x.str.contains('Python').sum())
print(seriesGropupobject)
concatdf=pd.concat([inputDf['Country'],seriesGropupobject],axis='columns',sort=False)
print("concatdf")

print(concatdf)

