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
print(table.sort_values(['age','experience'],ascending=[True,False])) 
print(table[['age','experience']])



