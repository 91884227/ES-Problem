#!/usr/bin/env python
# coding: utf-8

# # importy tool

# In[1]:


import pandas as pd
import numpy as np
from tqdm import tqdm


# In[2]:


class class_OnePlusOne:
    def __init__(self, Gamma_, 
                 Parent_ = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                 iteration_ = 10000000):
        self.Gamma = Gamma_
        self.Parent = Parent_
        self.iteration = iteration_ 
        # self.child
        
    def fit_func(self, list_):
        buf = [i**2 for i in list_]
        return( sum(buf) )
    
    def mutation(self):
        delta = np.random.normal(0, self.Gamma, len(self.Parent))
        self.Child = list(delta + self.Parent)
    
    def selection(self):
        if( self.fit_func(self.Child) <  self.fit_func(self.Parent) ):
            self.Parent = self.Child
        
    def Minimization(self):
        for i in tqdm(range(self.iteration)):
            if( self.fit_func(self.Parent) < 0.005):
                break
            self.mutation()
            self.selection()
        self.result = self.Parent
        self.result_fit = self.fit_func(self.Parent)
        self.time = i+1


# In[3]:


# test = ES(0.01, iteration_ = 10000)

# test.Minimization()

# print(test.result)
# print(test.result_fit)
# print(test.time)

