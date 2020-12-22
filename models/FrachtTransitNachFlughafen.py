import pandas as pd

df = pd.read_csv('C:/Users/marce/Desktop/uibk/FS1/Betriebliche Informaitonssysteme/miniTermProject/code/data/processable/table_2020-12-22_12-18-52_Transit_ankommend_nach_Flughaefen.csv',
                 header= [0,1],
                 index_col= [0,1],
                 delimiter= ';')


print(df.to_string())