import pandas as pd
import sqlite3

df=pd.read_csv('緊急搶修.csv')
df2=pd.read_csv('單位.csv')

# 2. 將 CSV 資料轉換為 SQLite 資料庫（在內存中創建資料庫）
conn = sqlite3.connect(':memory:')  # 創建一個內存資料庫
df.to_sql('緊急搶修', conn, index=False, if_exists='replace')
df2.to_sql('單位', conn, index=False, if_exists='replace')

query = """SELECT nos,area,dig_st,PLINE_CMP_ABBR
FROM 緊急搶修 
left join 單位 on 單位.PLINE_CMP_NO = 緊急搶修.ppcode ;"""
result = pd.read_sql(query, conn)

#result.to_html('output.html',index=False)
#result.to_csv('data.csv',index=False)
result.to_json('data.json', orient='records', force_ascii=False)
