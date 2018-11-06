#!/usr/bin/env python3
# -*- coding: utf-8 -
"""
Created on Tue Nov  6 19:56:24 2018

@author: ananya
"""

import numpy as np

P = np.array([[0, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0.5, 0.5, 0, 0], [0, 0.5, 0.5, 0, 0]])
V = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
alpha = 0.8

# smallest allowable error is epsilon
epsilon = 0.0000001


print(P)
print(V)

#C = V.transpose()
#print(V)


# This is  the equation for the steady state
pi0 = V.transpose()
k = (1 - alpha)*(V.transpose())
pi1 = alpha *(np.dot(P, V.transpose())) + k

error = np.linalg.norm((pi1 - pi0), ord=1)
print(error)


count = 0
while error > epsilon:
    # this is the iteration equation
    pi2 = alpha *(np.dot(P, pi1)) + k
    error = np.linalg.norm((pi2 - pi1), ord=1)
    pi1 = pi2
    count = count + 1
    

print("The loop ran for ", count, " times")   
print(pi2)

