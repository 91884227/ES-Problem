#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[1]:


import pandas as pd
import numpy as np
from tqdm import tqdm


# # import self-define module

# In[2]:

## 若要在同一級執行要
# from OnePlusOne import class_OnePlusOne
from module.OnePlusOne import class_OnePlusOne


# In[3]:


class class_OneOfFiveRule(class_OnePlusOne):
    def __init__(self, Gamma_, 
                 Parent_ = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                 iteration_ = 10000000):
        super().__init__(Gamma_, Parent_, iteration_)
        
        self.Gs = 0
    
    def selection(self):
        if( self.fit_func(self.Child) <  self.fit_func(self.Parent) ):
            self.Parent = self.Child
            self.Gs = self.Gs + 1
    
    def Minimization(self):
        for i in range(self.iteration):
            if( self.fit_func(self.Parent) < 0.005):
                break
            self.mutation()
            self.selection()
            
            if( self.Gs/(i+1) < 0.2):
                self.Gamma = self.Gamma*0.85
            elif( self.Gs/(i+1) > 0.2):
                self.Gamma = self.Gamma/0.85
            
        self.result = self.Parent
        self.result_fit = self.fit_func(self.Parent)
        self.time = i    


# In[4]:


# for i in tqdm(range(10)):
#     print("\nRun %d Start:" % (i+1))
#     test = Rule(1)
#     test.Minimization()
#     print("fit Parent: %s" % test.result)
#     print("fit value: %.6f" % test.result_fit)
#     print("iteration: %d" % test.time)

