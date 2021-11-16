#!/usr/bin/env python
# coding: utf-8

# In[27]:


import os
import pandas as pd


# In[28]:


df = pd.DataFrame()

for file in [file for file in os.listdir() if file.endswith('csv') and not file.startswith('cwe')]:
    
    print (file)
    df = pd.concat([df, pd.read_csv(file, index_col=False)], ignore_index=True)


# In[29]:


df.rename(columns={'CWE-ID': 'CWE_ID'}, inplace=True)
df.to_csv('cwe_descriptions.csv', index=False)

