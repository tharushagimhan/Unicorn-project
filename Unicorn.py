#!/usr/bin/env python
# coding: utf-8

# In[153]:


import pandas as pd
import numpy as np
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as mat


# In[154]:


df = pd.read_csv('E:\\python\\dataset.csv')


# In[155]:


df.head(10)


# In[156]:


df.shape


# In[157]:


df.info()


# In[158]:


df.size


# In[159]:


df.describe()


# In[160]:


df["Date Joined"] = pd.to_datetime(df["Date Joined"])


# In[161]:


df.info()


# In[162]:


df["Year Joined"] = df["Date Joined"].dt.year


# In[163]:


df.head()


# In[164]:


#sample
df_sample = df.sample(n=50 ,random_state = 42 )


# In[165]:


df_sample["Years"] = df_sample["Year Joined"] - df_sample["Year Founded"]


# In[166]:


#descriptive
grouped = (df_sample[["Industry","Years"]]).groupby("Industry").max().sort_values(by="Years")
grouped


# In[167]:


#bar chart
mat.bar(grouped.index,grouped["Years"])
mat.title("Industry vs Experience Years")
mat.xlabel("Industry")
mat.xticks(rotation=60,horizontalalignment='right')
mat.ylabel("Years of Experience")
mat.show()


# In[168]:


#anlyse with valuation
df_sample["New_Valuation"] = df_sample["Valuation"]
df_sample["New_Valuation"] = df_sample["New_Valuation"].str.replace('$','').str.replace('B','')
df_sample.head()


# In[169]:


# del df_sample["new"]


# In[170]:


df_sample.head()


# In[171]:


grouped =(df_sample[["Industry","New_Valuation"]]
          .groupby("Industry").max().sort_values("New_Valuation"))
grouped


# In[172]:


#bar chart2
mat.bar(grouped.index,grouped["New_Valuation"])
mat.title("Industry vs Valuation")
mat.xlabel("Industry")
mat.xticks(rotation=60, horizontalalignment='right')
mat.ylabel("Valuation")
mat.show()


# In[173]:


#data cleaning
df.drop_duplicates()


# In[174]:


df.drop_duplicates().shape


# In[175]:


df.info()


# In[176]:


# Sort by `companies`
df.sort_values(by='Company', ascending=True).head(10)


# In[177]:


df["Year Founded"].value_counts().sort_values(ascending=True)


# In[178]:


#histogram
sns.histplot(data=df,x='Year Founded')
mat.title('Year Founded')
mat.xlabel('Year')


# In[179]:


df["Month Joined"] = df["Date Joined"].dt.month
df["Month_name Joined"] = df["Date Joined"].dt.month_name()
df.head()


# In[180]:


df['Year Joined'].sort_values(ascending=False)


# In[181]:


df_2022 = df[df["Date Joined"].dt.year==2022]
df_2022.head()


# In[182]:


df_2022.insert(3,"Week Joined",df_2022["Date Joined"].dt.strftime('%Y-W%V'),True)
df_2022_week = df_2022.groupby(by="Week Joined")["Company"].count().reset_index().rename(columns={"Company":"Company Count"})
df_2022_week.head()


# In[190]:



month_order = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", 
               "December"]
print(month_order)


# In[195]:


df["Years"] = df["Date Joined"].dt.year - df["Year Founded"]
df.head(10)


# In[204]:


#boxplot
sns.boxplot(x=df['Month Joined'],
           y=df['Years'],
           showfliers=False)
mat.xticks(rotation=60,horizontalalignment='right')
mat.show()


# In[210]:


mat.figure(figsize=(10,6))
sns.barplot(x=df["Year Founded"],y=df["Years"],ci=False)
mat.xticks(rotation=60,horizontalalignment='right')
mat.show()


# In[214]:


mat.figure(figsize=(20,6))
sns.barplot(x=df_2022_week['Week Joined'],y=df_2022_week["Company Count"])


# In[ ]:




