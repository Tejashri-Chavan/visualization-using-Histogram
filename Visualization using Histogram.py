#!/usr/bin/env python
# coding: utf-8

# In[ ]:


TASK 3: Visualization using Histogram


# In[1]:


import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


data=pd.read_csv('Iris.csv')


# In[5]:


plt.xlabel('Petal Length (Cm)')
plt.ylabel('Frequency')
plt.title('Histogram of Petal Length')
plt.hist(data['PetalLengthCm'],bins=10,edgecolor='black')


# In[6]:


plt.show()


# In[ ]:




