#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 07:48:17 2018

@author: ananya
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 06:14:13 2018
@author: ananya

This program solves Expectation Maximization Problem.
"""

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
total = 500
runs = 15
log_arr= []
	

x_arr = np.empty([total])
p_arr = np.empty([total])	# array to hold the probabilities
mu_arr = np.empty([2])
var_arr = np.empty([2])
w_arr = np.empty([2])
log_points = []


def generate_samples_from_gaussian_mixture():
    sns.set()	#nice background for the plot
    samples = 0
    threshold = 0.5
    #x_arr = []	# array to hold the sample values of x	
    print(len(x_arr))
    while samples < total:
        xvals = np.random.normal(5, 1)	# Generate a random sample from the range of x
        U = np.random.uniform(0,1)
        
        if U <= threshold:
            xvals = np.random.normal(5, 1)
        else:
            xvals = np.random.normal(-5, 1)
		
        
        x_arr[samples]  = xvals
        samples = samples + 1
        #print(xvals)
	

generate_samples_from_gaussian_mixture()


#guess initial probabilities that a particular data point belongs to the first distribution
samples = 0
while samples < total:
    p_vals = np.random.uniform(0, 1)
    #print(p_vals)
    
    p_arr[samples] = p_vals
    samples = samples + 1


def calculate_mean_variance():
    sum1 = 0
    sum2 = 0
    div1 = 0
    div2 = 0
    for k in range(total):
        div1 = div1 +  p_arr[k]
    print("div1", div1)
    
    for j in range(total):
        div2 = div2 +  (1 - p_arr[j])
    print("div2", div2)
    for i in range(total):
        #print("x[i]", x_arr[i])
        #print("p[i]", p_arr[i])
        #print("p_arr", p_arr[i])
        sum1 = sum1 + (x_arr[i]*p_arr[i])
        sum2 = sum2 + (x_arr[i]*(1 - p_arr[i]))
        #div1 = div1 + p_arr[i]
        #div2 = div2 + (1 - p_arr[i])
    print("sum1", sum1)
    print("sum2", sum2)
        
    mu_arr[0] = sum1/div1
    mu_arr[1] = sum2/div2

    sum1 = 0
    sum2 = 0
    for l in range(total):
        sum1 = sum1 + ((x_arr[i] - mu_arr[0])*(x_arr[i] - mu_arr[0])*p_arr[i])
        sum2 = sum2 + ((x_arr[i] - mu_arr[1])*(x_arr[i] - mu_arr[1])*(1 - p_arr[i]))
    
    var_arr[0] = sum1/div1
    var_arr[1] = sum2/div2
    w_arr[0] = div1/total
    w_arr[1] = div2/total
    
def calculate_probability():
    for i in range(total):
        exp1 = np.exp(-np.square((x_arr[i]-mu_arr[0]))/(2*var_arr[0]))
        exp2 = np.exp(-np.square((x_arr[i]-mu_arr[1]))/(2*var_arr[1]))
        p_arr[i] = (((w_arr[0]/(np.sqrt(var_arr[0])))* exp1) + ((w_arr[1]/(np.sqrt(var_arr[0])))* exp2))/(np.sqrt(2*np.pi))

def calculate_gaussian(x, mu, sigma):
    exp1 = np.exp(-np.square((x-mu))/(2*np.square(sigma)))
for i in range(runs):
    calculate_mean_variance()
    print(mu_arr)
    print(var_arr)
    print(w_arr)
    print(p_arr)

#log_arr.append( np.log(w_arr[0]*calculate_gaussian(x_arr[i], mu_arr[0], \
            #np.sqrt(var_arr[0])) + w_arr[1]*calculate_gaussian(x_arr[i], \
            #mu_arr[1], np.sqrt(var_arr[1]))))




 

    