import pandas as pd
import sqlite3

df=pd.read_csv('案件編號5月.csv')
df2=pd.read_csv('5月檢討會-應報完工清單.csv')

# 2. 將 CSV 資料轉換為 SQLite 資料庫（在內存中創建資料庫）
conn = sqlite3.connect(':memory:')  # 創建一個內存資料庫
df.to_sql('五月報表', conn, index=False, if_exists='replace')
df2.to_sql('三月報表', conn, index=False, if_exists='replace')

query = """SELECT 案件編號
FROM 三月報表 
where 案件編號 in (select 案件編號 from 五月報表);"""
result = pd.read_sql(query, conn)

#result.to_html('output.html',index=False)
result.to_csv('data.csv',index=False)
#result.to_json('data.json', orient='records', force_ascii=False)
