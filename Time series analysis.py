#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
df = pd.read_csv("apple.csv",parse_dates = ['Date'],index_col = ['Date'])


# In[36]:


df.head()


# In[37]:


df.index


# In[39]:


df.rename(columns={'Close/Last':'close'},inplace = True)


# In[43]:


a = df['2024-02-01':'2024-02-15']
a


# In[58]:


df['Open'] = df['Open'].str.replace('$','')
df


# In[59]:


df['High'] = df['High'].str.replace('$','')
df


# In[60]:


df['Low'] = df['Low'].str.replace('$','')
df


# In[81]:


df['close'] = df['close'].apply(int)


# In[82]:


df.close.apply(type).value_counts()


# In[91]:


df.close.resample("M").mean().round(2)


# In[94]:


df_mean = df['close'].mean()
df_mean


# In[105]:


import matplotlib as plt
df['close'].plot()


# In[108]:


rng = pd.date_range(start='01-01-2020',end='31-12-2020',freq='M')
rng


# In[112]:


import numpy as np
ts = pd.Series(np.random.randint(1,10,len(rng)),index = rng)
ts


# In[118]:


df = ['2017-01-15','2017-02-16']
type(df)


# In[121]:


pd.to_datetime(df,errors="coerce")


# In[ ]:




