#!/usr/bin/env python
# coding: utf-8

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[1]:


import numpy as np


# #### Create an array of 10 zeros 

# In[2]:


arr=np.zeros(10)
print(arr)


# #### Create an array of 10 ones

# In[3]:


arr=np.ones(10)
print(arr)


# #### Create an array of 10 fives

# In[4]:


arr=np.ones(10)*5
print(arr)


# #### Create an array of the integers from 10 to 50

# In[5]:


arr=np.arange(10,51)
print(arr)


# #### Create an array of all the even integers from 10 to 50

# In[6]:


arr=np.arange(10,51,2)
print(arr)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[7]:


arr=np.arange(0,9).reshape(3,3)
print(arr)


# #### Create a 3x3 identity matrix

# In[8]:


arr=np.eye(3,3)
print(arr)


# #### Use NumPy to generate a random number between 0 and 1

# In[9]:


arr=np.random.rand(1)
print(arr)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[10]:


arr=np.random.rand(1,25)
print(arr)


# #### Create the following matrix:

# In[11]:


arr=np.arange(0.01,1.01,0.01).reshape(10,10)
print(arr)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[12]:


arr=np.linspace(0,1,20)
print(arr)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[13]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[16]:


temp=np.arange(1,26).reshape(5,5)


print(temp[2:,1:])

print(temp[3][-1])

print(temp[:3,1].reshape(3,1))

print(temp[-1])

print(temp[-2:])

print(temp.sum())

print(temp.std())

print(temp.sum(axis=0))


# In[ ]:




