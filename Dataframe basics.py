#!/usr/bin/env python
# coding: utf-8

# In[5]:


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


# In[ ]:





# In[ ]:




