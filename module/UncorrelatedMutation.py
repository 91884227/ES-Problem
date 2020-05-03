#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[1]:


import pandas as pd
import numpy as np
from tqdm import tqdm
import math


# # import self-define module

# In[2]:


from module.OnePlusOne import class_OnePlusOne


# In[3]:


class class_UncorrelatedMutation(class_OnePlusOne):
    def __init__(self, Gamma_, 
                 Parent_ = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                 iteration_ = 10000000):
        super().__init__(Gamma_, Parent_, iteration_)
        self.tao = 0.0002
        self.taopron = 0.0003
        self.epsilon = 0.001
        self.epsilon_list = list(np.repeat(self.epsilon, len(self.Parent)))
        self.Gamma_list = list(np.repeat(self.Gamma, len(self.Parent)))
    
    def mutation(self):
        N_01 = np.random.normal(0, 1, 1)[0]
        Ni_01 = np.random.normal(0, 1, 10)
        buf = [self.Gamma_list[i]*math.exp(self.taopron*N_01 + self.tao*Ni_01[i]) 
               for i in range(len(self.Gamma_list))]
        
        self.Gamma_list = max(buf,  self.epsilon_list)
        
        self.Child = [self.Parent[i] + self.Gamma_list[i]*Ni_01[i] 
                      for i in range(len(self.Parent))]  
        


# In[4]:


# for i in tqdm(range(1)):
#     print("\nRun %d Start:" % (i+1))
#     func = class_UncorrelatedMutation(0.1)
#     func.Minimization()
#     print("fit Parent: %s" % func.result)
#     print("fit value: %.6f" % func.result_fit)
#     print("iteration: %d" % func.time)


# In[5]:


# Ni_01 = np.random.normal(0, 1, 10)

# test = class_UncorrelatedMutation(1)

# test.tao*Ni_01

# N_01 = np.random.normal(0, 1, 1)[0]
# Ni_01 = np.random.normal(0, 1, 10)

# buf = [self.Gamma_list[i]*math.exp(self.taopron*N_01 + self.tao*Ni_01[i]) 
#  for i in range(len(self.Gamma_list))]

# self.Gamma_list = max(buf,  self.epsilon_list)

# self.Child = [self.Parent[i] + self.Gamma_list[i]*Ni_01[i] 
#  for i in range(len(self.Parent))]

# test.Child

