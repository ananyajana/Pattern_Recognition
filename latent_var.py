#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 09:04:56 2018

@author: aj611

"""

# Program for latent variable problem
from math import exp, pow
#from sympy import *
#import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#from random import *
import time
import pdb

samples = 0
ELEMS = 500
X_arr = (2, ELEMS)

def cov(x, y):
    xbar, ybar = x.mean(), y.mean()
    return np.sum((x - xbar)*(y - ybar))/(len(x) - 1)

# Covariance matrix
def cov_mat(X):
    return np.array([[cov(X[0], X[0]), cov(X[0], X[1])], \
                     [cov(X[1], X[0]), cov(X[1], X[1])]])	
for i in range(50):
    sns.set()	#nice background for the plot
    samples = 1
    total = 500	# total number of valid x samples that we want to generate
    x1_arr = []	# array to hold the sample values of x	
    print(len(x1_arr))
    x2_arr = []
    while samples <= total:
        x1vals = np.random.normal(1, np.sqrt(2.1))
        x2vals = np.random.normal(-1, np.sqrt(0.1))
    		
        samples = samples + 1
        x1_arr.append(x1vals)
        x2_arr.append(x2vals)
        #print("Vector: ", samples)
        #print(x1vals)
        #print(x2vals)
        #X_arr = (2, ELEMS)
        X_arr = [(x1vals, x2vals) for i in range(total+1)]
        #print(X_arr)
        #np.zeros(X_arr)
        #X_arr[1].append(x1vals)
        #X_arr[2].append(x2vals)
    
    X = np.array([x1_arr, x2_arr])
    #print(X)
    
    Mu1 = np.mean(x1_arr)
    var1 = np.var(x1_arr)
    print("Mu1: ")
    print(Mu1)
    print("var1: ")
    print(var1)
    
    
    
    
    Mu2 = np.mean(x2_arr)
    var2 = np.var(x2_arr)
    print("Mu2: ")
    print(Mu2)
    print("var2: ")
    print(var2)
    
    Mu = np.array([Mu1, Mu2])
    covar = np.empty([2, 2])
    
    
    
    # Calculate covariance matrix 
    M = cov_mat(X.T)
    print(M) # (or with np.cov(X.T))
    
    avg_mean_square_error_classical = (1/4)*((M[0,0] - 2.1)*(M[0,0] - 2.1) + (M[0,1] - 0)*(M[0,1] - 0) + (M[1,0] - 0)*(M[1,0] - 0) + (M[1,1] - 0.1)*(M[1,1] - 0.1))#i = 1
    print("average mean square error using classical method:")
    print(avg_mean_square_error_classical)
    
    avg_mean_square_error_special = (1/4)*((var1 - 2.1)*(var1 - 2.1) + (var2 - 0.1)*(var2 - 0.1))#i = 1
    print("average mean square error using special method:")
    print(avg_mean_square_error_special)
    
    #for i in range(501):
    #    covar[i] = np.dot()


    

    