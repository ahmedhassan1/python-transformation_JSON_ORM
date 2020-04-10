#step 0
import pandas as pd
energy = pd.read_excel('data/Energy Indicators.xls',skiprows = range(1,18),skipfooter = 38,header = 0,usecols=range(2,6),names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'],na_values=['...'])                            
energy['Energy Supply']=energy['Energy Supply']*1000000

#begining of function
def delete_nums(text):
    
    clean_list = [item for item in text if (not item.isdigit() and item != "(" and item != ")" ) ]
    clean_text="".join(clean_list)
    
    return clean_text
#end of function
energy['Country'] = energy['Country'].apply(delete_nums)


# replaccing values
energy["Country"].replace({"Republic of Korea": "South Korea", "United States of America": "United States",
                           "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                           "China, Hong Kong Special Administrative Region": "Hong Kong",
                           "Bolivia Plurinational State of": "Bolivia","Iran Islamic Republic of":"Iran"}, inplace=True)

#deleting numbers and parnthes 



energy.head(20)

#step1
GDP = pd.read_csv('data/world_bank.csv',skiprows = range(0,4),header=0) 
GDP["Country Name"].replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran",
                           "Hong Kong SAR, China": "Hong Kong"}, inplace=True)
GDP.rename(columns = {'Country Name' : 'Country'}, inplace = True)
GDP.head(50)

#step 2
ScimEn= pd.read_excel('data/scimagojr-3.xlsx')
ScimEn.head(50)

#step3
print('entries of energy',energy.shape[0])
print('entries of GDP',GDP.shape[0])
print('entries of ScimEn',ScimEn.shape[0])
Energy_GDP = pd.merge(energy,[GDP['Country','2006', '2007', '2008','2009','2010','2011','2012','2013','2014','2015']],on='Country')
Energy_GDP.set_index('Country', inplace = True)
print('entries of Energy_GDP',Energy_GDP.shape[0])
#Energy_GDP.head(90)


#step4
Energy_GDP_ScimEn=pd.merge(ScimEn[(ScimEn['Rank'] <= 15) ],Energy_GDP,on='Country')
Energy_GDP_ScimEn.set_index('Country', inplace = True)
#print('entries of Energy_GDP_ScimEn',Energy_GDP_ScimEn.shape[0])

print('shape of Energy_GDP_ScimEn',Energy_GDP_ScimEn.shape)
Energy_GDP_ScimEn.head(20)

#step5
step5= Energy_GDP_ScimEn[['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
#avgGDP1=avgGDP.mean()
#avgGDP=Energy_GDP_ScimEn[Country].groupby('Country').sum()
#avgGDP.head(20)
avgGDP=step5.sum(axis = 1, skipna = True) / 10
avgGDP.sort_values(ascending=False)

#step6
print(Energy_GDP_ScimEn['Energy Supply per Capita'].mean())

#step7

#Energy_GDP_ScimEn.head()
step7=Energy_GDP_ScimEn[['% Renewable']]
t = (step7['% Renewable'].idxmax(), step7['% Renewable'].max())
print(t)

#step8
Energy_GDP_ScimEn['ratio of Self-Citations to Total Citations'] = Energy_GDP_ScimEn['Self-citations'] / Energy_GDP_ScimEn['Citations']
step8=Energy_GDP_ScimEn[['ratio of Self-Citations to Total Citations']]
#print(step8[step8['ratio of Self-Citations to Total Citations'] == step8['ratio of Self-Citations to Total Citations'].max()])
t1 = (step8['ratio of Self-Citations to Total Citations'].idxmax(), step8['ratio of Self-Citations to Total Citations'].max())
t1

#step9
Energy_GDP_ScimEn['HighRenew'] = Energy_GDP_ScimEn['% Renewable'].apply(lambda x : '1' if x >= Energy_GDP_ScimEn['% Renewable'].mean() else '0' )
HighRenew=Energy_GDP_ScimEn['HighRenew']
HighRenew.sort_values(ascending=False)

#step10
Energy_GDP_ScimEn['Population']=Energy_GDP_ScimEn['Energy Supply'] / Energy_GDP_ScimEn['Energy Supply per Capita'] 
Energy_GDP_ScimEn['Populationbymilion']=Energy_GDP_ScimEn['Population'] / 1000000
Energy_GDP_ScimEn.head(20)

from pandas import DataFrame
df2 = pd.DataFrame(list(ContinentDict.items()),columns = ['Country','continent'])
#df2.set_index('Country', inplace = True)
df2.head(20)

merged = pd.merge(df2,Energy_GDP_ScimEn['Population'], on='Country' )
merged.head(20)

