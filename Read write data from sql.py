#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
w = {"name":['ajay','vijay','mohan','yuvi','rohan'],
    "temp":[32,25,52,85,74],
    "windspeed":[6,7,2,4,2]}
df = pd.DataFrame(w)
print(df)


# In[6]:


df.shape


# In[7]:


rows,columns = df.shape
print(rows)
print(columns)


# In[8]:


df.head(2)


# In[9]:


df.tail(2)


# In[10]:


df[2:4]


# In[11]:


df.columns


# In[12]:


df2 = df[["temp",'windspeed']]
df2


# In[13]:


type(df["temp"])


# In[14]:


df["temp"].max()
df["temp"].min()


# In[15]:


df.describe()


# In[16]:


df[df.temp>52]


# In[17]:


df.index


# In[18]:


df.set_index("temp",inplace = True)
df


# In[19]:


df.loc[25]


# In[20]:


df.reset_index(inplace = True)
df


# In[34]:


new_row = {"temp":31,"name":"sohan"}
df.append(new_row, ignore_index=True)
df


# In[35]:


df2 = df.fillna(0)
df2


# In[36]:


df2 = df.fillna(method = "ffill")
df2


# In[37]:


df2 = df.interpolate()
df2


# In[38]:


df2 = df.dropna()
df2


# In[43]:


import numpy as np
df2 = df.replace(np.NaN,8)
df2


# In[46]:


df2 = df.replace({"windspeed":"[A-Za-z]"},' ',regex = True)
df2


# In[49]:


w = {'temp':[10,20,30],
    'name':["r","n","v"],
    'windspeed': [6,7,8]}
df2 = pd.DataFrame(w)
df2


# In[50]:


pd.concat([df,df2])


# In[51]:


pd.concat([df,df2],ignore_index = True)


# In[54]:


temp_df = pd.DataFrame({'city':['delhi',"mumbai",'kolkata'],"temp":[10,20,30]},index = [0,1,2])
temp_df


# In[63]:


wind_df = pd.DataFrame({'city':['mumbai','delhi'],'wind':[1,2]},index=[1,0])
wind_df


# In[64]:


df2 = pd.concat([temp_df,wind_df],axis = 1)
df2


# In[65]:


df3 = pd.merge(temp_df,wind_df,on = 'city')
df3


# In[72]:


df4 = pd.merge(temp_df,wind_df,on = 'city', how ='left')
df4


# In[74]:


df5 = pd.merge(temp_df,wind_df,on = 'city',how= 'right')
df5


# In[3]:


df = pd.read_csv("weather.csv")
df


# In[4]:


df2 = df.groupby("city")
df2


# In[14]:


for city,city_df in df2:
    print(city)
    print(city_df)


# In[17]:


df2.get_group("mumbai")


# In[18]:


df2.max()


# In[21]:


df2.describe()


# In[26]:


df2["humidity"].mean().round(2)


# In[29]:


df.pivot(index="date",columns='city')


# In[30]:


df = pd.read_csv("weather2.csv")
df


# In[32]:


df.pivot_table(index= 'city',columns='date')


# In[33]:


df.pivot_table (index= "city",columns="date",aggfunc= sum)


# In[41]:


df = pd.read_csv("weather3.csv")
df['date'] = pd.to_datetime(df['date'])


# In[45]:


df


# In[43]:


type(df['date'][0])


# In[47]:


df.pivot_table(index=pd.Grouper(freq = 'M',key= 'date'),columns ="city").round(2)


# In[2]:


import sqlalchemy as sa


# In[90]:


engine = sa.create_engine("mysql+pymysql://root:rishi@localhost:3306/students")


# In[91]:


#df = pd.read_sql_table("student",engine)
connection = engine.connect()
df = pd.read_sql_table("student",connection)
connection.close()
df


# In[42]:


df[["name",'course','school']]


# In[75]:


connection = engine.connect()
query=sa.text("select round(avg(income)) as average_value from student where course like 'b%'")
df = pd.read_sql_query(query,connection)
connection.close()
df


# In[77]:


connection = engine.connect()
query=sa.text("select*from student")
df = pd.read_sql(query,connection)
connection.close()
df


# In[82]:


customer = {'id':[106,107,108],
           'name':['ayush','tanay','nisha'],
           'course':['interior','architect','bba'],
           'school':['ASAP','ASAP','ABS'],
           "NUM":[486116,98494,8984],
           "INCOME":[16000,14000,12000]}
df2 = pd.DataFrame(customer)
df2


# In[87]:


df2.to_sql(
name = 'student',
con = engine,
index= False,
if_exists = 'append')


# In[92]:


connection = engine.connect()
query=sa.text("select*from student")
df = pd.read_sql(query,connection)
connection.close()
df


# In[ ]:




