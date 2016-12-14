import zipfile
import numpy as np
import pandas as pd
from prettytable import PrettyTable
import math as mt

print('#'*55)
print('#'*2 + ' Rassembler les deux fichiers dans un même dataframe')
print('#'*2 + ' Objectif : Analyser l\'ensemble des données')
print('#'*55)

ziptrain = zipfile.ZipFile('data.zip') # Les deux fichiers (train et test sont) sont mis dans un dossier zip

df=[]

for f in range(0,len(ziptrain.namelist())):
    if (f == 0):
        df    = pd.read_csv(ziptrain.open(ziptrain.namelist()[f]), sep=';')
    else:
        my_df = pd.read_csv(ziptrain.open(ziptrain.namelist()[f]), sep=';')
        df    = (pd.DataFrame(np.concatenate((df,my_df),axis=0), 
                              columns=list(my_df.columns.values)))

#print(list(df.groupby(['COD_INSEE'])['ID'].count()))
#print(df.count())
#df.to_csv(path_or_buf='tout.csv', sep=';')
df_dep = df.dropna(axis=1, how='any')
col = df_dep.apply(lambda row : '0' + str(mt.floor(row[0]/1000)) if row[0] < 10000 else str(mt.floor(row[0]/1000)), axis = 1 )
df_dep['DEPT'] = col

#df_dep.to_csv(path_or_buf='tout.csv', sep=';')

x = PrettyTable()
listeC = ['C1', 'C2', 'DEPT']
x.field_names = listeC
for i in listeC:
    gr = df_dep.groupby(by=i)['ID']
    nb = gr.count()
    #print(nb.sort_index(ascending=False))
    
print(x)