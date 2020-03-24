#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 
column_names = ['user_id', 'item_id', 'rating', 'timestamp'] 
path = 'file.tsv'
df = pd.read_csv(path, sep='\t', names=column_names)  
df.head() 


# In[5]:


movie_titles = pd.read_csv('Movie_Id_Titles.csv') 
movie_titles.head(50) 


# In[6]:



data = pd.merge(df, movie_titles, on='item_id') 
data.head(70)


# In[7]:


gk = data.groupby('title')
gk['rating'].mean().sort_values(ascending=False).head(100)


# In[8]:


gk['rating'].count().sort_values(ascending=False).head()


# In[9]:


ratings = pd.DataFrame(gk['rating'].mean())


# In[10]:


ratings['num of ratings'] = pd.DataFrame(gk['rating'].count())


# In[11]:


ratings.head(100) 


# In[12]:


import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set_style('white') 
get_ipython().run_line_magic('matplotlib', 'inline')

plt.figure(figsize =(10, 5)) 

ratings['num of ratings'].hist(bins = 100) 


# In[13]:



plt.figure(figsize =(10, 5)) 

ratings['rating'].hist(bins = 70) 


# In[14]:


moviemat = data.pivot_table(index ='user_id', columns ='title', values ='rating') 
moviemat.head(10) 


# In[15]:


ratings.sort_values('num of ratings', ascending = False).head(10)


# In[16]:


starwars_user_ratings = moviemat['Star Wars (1977)'] 
liarliar_user_ratings = moviemat['Liar Liar (1997)']
starwars_user_ratings.head() 


# In[18]:


similar_to_starwars = moviemat.corrwith(starwars_user_ratings) 
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings) 

corr_starwars = pd.DataFrame(similar_to_starwars, columns =['Correlation']) 
corr_starwars.dropna(inplace = True) 

corr_starwars.head() 


# In[46]:


corr_starwars.sort_values('Correlation', ascending = False) 
corr_starwars = corr_starwars.join(ratings['num of ratings']) 

corr_starwars.head() 

corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending = False).head(10) 


# In[47]:


corr_liarliar = pd.DataFrame(similar_to_liarliar, columns =['Correlation']) 
corr_liarliar.dropna(inplace = True) 

corr_liarliar = corr_liarliar.join(ratings['num of ratings']) 
corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation', ascending = False).head() 


# In[ ]:




