#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# In[3]:


df = pd.read_csv('C:\\Users\\ASUS\\Downloads\\USvideos.csv')


# In[4]:


df.head()


# In[6]:


df.shape


# In[8]:


df = df.drop_duplicates()
df.shape


# In[9]:


df.describe()


# In[10]:


df.info()


# In[12]:


columns_to_remove = ['thumbnail_link' , 'description']
df = df.drop(columns=columns_to_remove)
df.info()


# In[13]:


from datetime import datetime


# In[14]:


import datetime


# In[15]:


df["trending_date"] = df["trending_date"].apply(lambda x : datetime.datetime.strptime(x, '%y.%d.%m'))
df.head()


# In[16]:


df['publish_time'] = pd.to_datetime(df['publish_time'])
df.head()


# In[17]:


df['publish_month'] = df['publish_time'].dt.month
df['publish_day'] = df['publish_time'].dt.day
df['publish_hour'] = df['publish_time'].dt.hour
df.head(2)


# In[18]:


df['category_name'] = np.nan
df.loc[(df["category_id"] == 1), "category_name"] = 'film and animation'
df.loc[(df["category_id"] == 2), "category_name"] = 'autos and vehicles'
df.loc[(df["category_id"] == 10), "category_name"] = 'music'
df.loc[(df["category_id"] == 15), "category_name"] = 'pets and animals'
df.loc[(df["category_id"] == 17), "category_name"] = 'sports'
df.loc[(df["category_id"] == 19), "category_name"] = 'travel and events'
df.loc[(df["category_id"] == 20), "category_name"] = 'gaming'
df.loc[(df["category_id"] == 22), "category_name"] = 'people and blogs'
df.loc[(df["category_id"] == 23), "category_name"] = 'comedy'
df.loc[(df["category_id"] == 24), "category_name"] = 'entertainment'
df.loc[(df["category_id"] == 25), "category_name"] = 'news and politics'
df.loc[(df["category_id"] == 26), "category_name"] = 'how to and style'
df.loc[(df["category_id"] == 27), "category_name"] = 'education'
df.loc[(df["category_id"] == 28), "category_name"] = 'science and technology'
df.loc[(df["category_id"] == 29), "category_name"] = 'non profits and activism'
df.loc[(df["category_id"] == 30), "category_name"] = 'movies'
df.loc[(df["category_id"] == 43), "category_name"] = 'shows'
df.head()


# In[19]:


df['year'] = df['publish_time'].dt.year
yearly_counts = df.groupby('year')['video_id'].count()
#create bar chart
yearly_counts.plot(kind='bar' , xlabel='year',ylabel='total publish count',title='total publish video per year')
#show the chart
plt.show()


# In[21]:


yearly_views = df.groupby('year')['views'].sum
#create bar chart
yearly_counts.plot(kind='bar' , xlabel='year',ylabel='total views',title='total viewsper year')
plt.xticks(rotation = 0)
plt.tight_layout()
#show the chart
plt.show()


# In[22]:


category_views = df.groupby('category_name')['views'].sum().reset_index()
#start the categories by views in descending order 
top_categories = category_views.sort_values(by = 'views' , ascending = False).head(5)
#create a bar plot to visualize the top 5 categories
plt.bar(top_categories['category_name'],top_categories['views'])
plt.xlabel('category Name',fontsize = 11)
plt.ylabel('total views',fontsize = 12)
plt.title('top 5 categories',fontsize = 15)
plt.tight_layout()
plt.show()


# In[23]:


plt.figure(figsize=(12, 6))
sns.countplot(x='category_name' , data=df, order=df['category_name'].value_counts().index)
plt.xticks(rotation = 90)
plt.title('video count by category')
plt.show()


# In[24]:


#counting the number of videos published per hour
videos_per_hour = df['publish_hour'].value_counts().sort_index()
#create a bar plot
plt.figure(figsize = (12,6))
sns.barplot(x=videos_per_hour.index,y=videos_per_hour.values,palette='rocket')
plt.title('number of videos published per hour')
plt.xlabel('hour of day')
plt.ylabel('number of videos')
plt.xticks(rotation = 45)
plt.show()


# In[25]:


df['publish_time'] = pd.to_datetime(df['publish_time'])
df['publish_date'] = df['publish_time'].dt.date
video_count_by_date = df.groupby('publish_date').size()
plt.figure(figsize = (12,6))
sns.lineplot(data=video_count_by_date)
plt.title("videos published over time")
plt.xlabel("publish date")
plt.ylabel("number of videos")
plt.xticks(rotation = 45)
plt.show()


# In[26]:


#scatter plot between 'views and likes'
sns.scatterplot(data=df,x='views',y='likes')
plt.title('views vs likes')
plt.xlabel('views')
plt.ylabel('likes')
plt.show()


# In[28]:


plt.figure(figsize=(14,8))
plt.subplots_adjust(wspace = 0.2,hspace = 0.4,top = 0.9)
plt.subplot(2,2,1)
g = sns.countplot(x='comments_disabled',data=df)
g.set_title("comments disabled",fontsize=16)
plt.subplot(2,2,2)
g1 = sns.countplot(x='ratings_disabled',data=df)
g1.set_title("rating disabled",fontsize = 16)
plt.subplot(2,2,3)
g2 = sns.countplot(x='video_error_or_removed',data=df)
g2.set_title("video error or removed",fontsize = 16)
plt.show()


# In[30]:


corr_matrix = df['views'].corr(df['likes'])
corr_matrix


# In[ ]:




