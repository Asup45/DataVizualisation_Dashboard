#!/usr/bin/env python
# coding: utf-8

# In[3]:


titanic = sns.load_dataset('titanic')
titanic.head()


# In[4]:


titanic.drop(['alone', 'alive', 'who', 'adult_male', 'embark_town', 'class'], axis=1, inplace=True)
titanic.dropna(axis=0, inplace=True)
titanic.head()


# In[5]:


sns.pairplot(titanic)


# In[9]:


sns.boxplot(x='pclass', y='age', data=titanic, hue='sex')


# In[13]:


sns.displot(titanic['fare'])


# In[18]:


sns.jointplot(x='age', y='fare', data=titanic, kind='hex')

