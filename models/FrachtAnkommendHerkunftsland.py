import pandas as pd
from tabulate import tabulate


df = pd.read_csv('C:/Users/marce/Desktop/uibk/FS1/Betriebliche Informaitonssysteme/miniTermProject/code/data/processable/table_2020-12-22_12-16-26_Fracht_Post_ankommend_Herkunftsland.csv',
                 header= [0,1],
                 index_col= [0,1],
                 delimiter= ';')


print(tabulate(df, headers='keys', tablefmt='psql'))