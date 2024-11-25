import pandas as pd

# Загрузка CSV файла
table = pd.read_csv("11.csv",index_col = 0)
for ele,ele2 in table.iterrows():
    table.loc[ele,'Big City'] = ele2['city'].upper()
#table["length"] = table["name"].apply(len)

print(table)
#print(table.head())
#print(table.info())
#print(table.shape)
#print(table.describe())

#print(table.values)
#print(table.index)
#print(table.columns)
#print(table.sort_values(['age','experience'],ascending=[True,False])) 
#print(table[['age','experience']])

print(table['age'].mean())   #center of my data
print(table['age'].median()) #median of data
#print(table['age'].max())
#print(table['age'].min())  
#print(table['age'].sum())  
print(table['age'].mode()) #idk what it does
print(table['age'].var())   #suppose to be variation
print(table['age'].std())   #suppose to be standart variation
print(table['age'].quantile(0.3))    
table['age'].agg([function]) #makes a column throght the function




