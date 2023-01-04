#!/usr/bin/env python
# coding: utf-8

# # Python Codes on 03/01/2023

# # Group Anagrams

# # Problem Statement
# 
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# 
# 

# In[4]:


#Source code
def groupAnagrams(strs):
    d = {}        
    for i in strs:
        key = "".join(sorted(i))
        if key not in d:
            d[key] = [i]            
        else:
            d[key].append(i)                
    return d.values()

    


# In[5]:


strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)


# # Product of Array Except Self

# # Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]
# 
#  

# In[11]:


from math import prod


# In[14]:


def productExceptSelf(nums):
    g=[1]*(len(nums))
    for i in range(0,len(g)):
        g[i]=prod(nums[:i]+nums[i+1:])
    return g


# In[15]:


nums=[1,2,3,4]
productExceptSelf(nums)


# In[ ]:




