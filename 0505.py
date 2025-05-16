import pandas as pd
import numpy as np
#data = [
#    {"name": "Alice", "age": 25, "department": "HR", "salary": 50000},
#    {"name": "Bob", "age": 30, "department": "IT", "salary": 60000},
#    {"name": "Charlie", "age": 22, "department": "Finance", "salary": 55000},
#    {"name": "David", "age": 35, "department": "IT", "salary": 70000},
#    {"name": "Eva", "age": 28, "department": "HR", "salary": 52000}
#]
#df=pd.DataFrame(data)
df=pd.read_csv('失業的教育程度類別.csv')
#df=df.groupby('area')['nos'].count().reset_index()
#df=df.query('單位=="台灣自來水股份有限公司第六區管理處新營營運所" or 單位=="中華電信公司台南營運處第二客網中心"')
#df.sort_values(by='單位').to_html('output.html',index=False)
#df['你是七股區嗎?']=np.where(df['area']=='七股區','我是七股區','我不是七股區')
df=df.query('性別=="總計"')

#df.to_html('output.html',index=False)
df.to_json('失業的教育程度類別.json',orient='records', force_ascii=False)

#newdf=pd.DataFrame(newdata)
#df=pd.concat([df,newdf],ignore_index=True)

#print('後來的資料')
#print(df)
