#!/usr/bin/env python
# coding: utf-8

# # Assignment
# 
# # Task1:
# 
# Wuzzuf jobs in Egypt data set at Kaggle
# 
# https://www.kaggle.com/omarhanyy/wuzzuf-jobs
# 
# Build all python needed classes to get the following from the Wuzzuf jobs in Egypt data set:
# 
# 1.	Read the dataset, convert it to DataFrame and display some from it.
# 
# 2.	Display structure and summary of the data.
# 
# 3.	Clean the data (null, duplications)
# 
# 4.	Count the jobs for each company and display that in order (What are the most demanding companies for jobs?)
# 

# ## Wuzzuf Egypt Jobs Postings EDA
# 
# Contents
# 
# 1. Introduction
# 
# 2. Data Wrangling
# 
# 3. Exploratory Data Analysis

# # 1. Introduction
# 
# This dataset includes 4380 Jobs with attributes such as Title, Company, Location, Type ,Level ,YearsExp ,Country , Skills.
# 
# This is an exploratory data analysis project to discover hidden trends in the Egyptian job postings on Wuzzuf.

# In[135]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # 2. Data Wrangling
# 

# In[136]:



# Import CSV file and output header
file = "Wuzzuf_Jobs.csv"
df = pd.read_csv(file)
df.head()


# In[137]:


# Structure Of Data
df.shape


# In[138]:


#Here we can see some informations about data like number of rows and data types .
df.info()


# In[139]:


df.isnull().any()


# Hint : AS we can see from previous informations our data haven't null values > This is so clear now .

# In[140]:


# Some statstics about data 
df.describe()


# In[141]:


# Checking for any duplicates values
df.duplicated().sum()


# In[142]:


# Get duplicates rows
duplicates = df.duplicated()
df[duplicates] 


# In[143]:


# Drop duplicates
df.drop_duplicates(inplace = True)


# In[144]:


# Confirmaing no duplicates values now
df.duplicated().sum()


# # 2. Exploratory Data Analysis

# In[145]:


# What are the most demanding companies for jobs?
demanding_companies = df['Company'].value_counts().head(10)
print(demanding_companies)


# In[146]:


# pie chart graph for display top 10 companies.
demanding_companies.plot(kind='pie',figsize=(8 ,8) )
plt.title('Top 10 Companies in Wuzzuf' ,fontsize = 15)
plt.legend();


# Hint : The most company attract jops is Confidential .                                      

# In[147]:


# What are it the most popular job titles?
popular_jop =  df['Title'].value_counts().head(10)
print(popular_jop)


# In[148]:


# bar chart graph for display top 10 jops.
popular_jop.plot(kind='barh' ,figsize=(8,8))
plt.title('Top 10 Wuzzuf Jobs Needed' ,fontsize = 15)
plt.legend()


# Hint : The most jop appear in our search is Accountant .                                      

# In[149]:


# What are the most popular areas?
popular_area = df["Country"].value_counts().head(10)

print(popular_area)


# In[150]:


# bar chart graph for display top 10 areas.
popular_area.plot(kind='barh' ,figsize=(8,8))
plt.title('Top 10 Areas At Wuzzuf  Needed Jops' ,fontsize = 15)
plt.legend()


# In[151]:


# What are the most popular Locations?
popular_location = df["Location"].value_counts().head(10)
print(popular_area)


# In[152]:


# bar chart graph for display top 10 locations.
popular_location.plot(kind='barh' ,figsize=(8,8))
plt.title('Top 10 locations At Wuzzuf  Needed Jops' ,fontsize = 15)
plt.legend()


# In[153]:


# What are the most important skills required?
df["Skills"].value_counts().head()


# In[154]:


import collections
List_df=list(df["Skills"])
mapDic={}
ListString =",".join(ListDf).split(",")
CounterSkills = collections.Counter(ListString)
SkillDF = pd.DataFrame.from_dict(CounterSkills , orient='index' ,columns=["SkillCount"])
SkillDF

