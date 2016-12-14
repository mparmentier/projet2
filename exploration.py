import pandas as pd

df = pd.read_csv('training_inputs.csv', sep=';')
print(df.groupby(['COD_INSEE'])['ID'].count())