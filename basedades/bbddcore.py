import pandas as pd
import sqlite3

llista_taules = pd.read_excel('../auxfiles/webdades.xlsx', index_col=0)
print(llista_taules)

conn = sqlite3.connect('../basedades/enercomm.db')
c = conn.cursor()

for taula in llista_taules.namestaula:
    arxiu = '../auxfiles/' + taula + '.xlsx'
    taulaimp = pd.read_excel(arxiu, index_col=0)
    taulaimp.to_sql(taula, con=conn, if_exists='replace')

c.close()