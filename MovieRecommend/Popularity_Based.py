#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
column_names = ['user_id', 'item_id', 'rating', 'timestamp'] 
path = 'file.tsv'
df = pd.read_csv(path, sep='\t', names=column_names)  
df.head() 


# In[3]:


movie_titles = pd.read_csv('Movie_Id_Titles.csv') 
movie_titles.head(50) 


# In[4]:



data = pd.merge(df, movie_titles, on='item_id') 
data.head(70)


# In[5]:


gk = data.groupby('title')
gk['rating'].mean().sort_values(ascending=False).head(100)


# In[6]:


gk['rating'].count().sort_values(ascending=False).head()


# In[7]:


ratings = pd.DataFrame(gk['rating'].mean())


# In[8]:


ratings['num of ratings'] = pd.DataFrame(gk['rating'].count())


# In[9]:


ratings.head(100) 


# In[10]:


import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set_style('white') 
get_ipython().run_line_magic('matplotlib', 'inline')

plt.figure(figsize =(10, 5)) 

ratings['num of ratings'].hist(bins = 100) 


# In[11]:



plt.figure(figsize =(10, 5)) 

ratings['rating'].hist(bins = 70) 


# In[17]:


print("Highly popular and highest rated movies are(TOP TEN):")
ratings.sort_values('num of ratings', ascending = False).head(10)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




