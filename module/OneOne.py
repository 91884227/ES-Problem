#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[1]:


import pandas as pd
import numpy as np
from tqdm import tqdm


# # import self-define tool

# In[2]:


from module.OnePlusOne import class_OnePlusOne


# In[3]:


class class_OneOne(class_OnePlusOne):
    def selection(self):
        self.Parent = self.Child    


# In[4]:


# for i in tqdm(range(1)):
#     print("\nRun %d Start:" % (i+1))
#     func = class_OneOne(0.01)
#     func.Minimization()
#     print("fit Parent: %s" % func.result)
#     print("fit value: %.6f" % func.result_fit)
#     print("iteration: %d" % func.time)

