#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 21:50:23 2018

@author: ananya
"""

import numpy as np


# this function is inspired by the code at http://www.quuxlabs.com/wp-content/uploads/2010/09/mf.py_.txt
def UV_decomposition(R, P, Q, K, steps=5000, alpha=0.0002, beta=0.02):
    Q = Q.T
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - np.dot(P[i,:],Q[:,j])
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
        eR = np.dot(P,Q)
        e = 0
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - np.dot(P[i,:],Q[:,j]), 2)
                    for k in range(K):
                        e = e + (beta/2) * ( pow(P[i][k],2) + pow(Q[k][j],2) )
        if e < 0.001:
            break
    return P, Q.T

M = np.array([[2, 1, 0, 1, 0, 5], 
              [4, 0, 2, 0, 0, 0], 
              [3, 3, 0, 5, 1, 0], 
              [0, 0, 5, 0, 1, 2]])
#M = np.array([[2, 1, , 1, , 5], [4, , 2, , , ], [3, 3, , 5, 1, ], [, , 5, , 1, 2]])
#print(np.sum(np.sum(M)))
print("sum of all elems", np.sum(M))
print("count of non-zero elems", np.count_nonzero(M))
# this average considers only non-blank elements
average = np.sum(M)/np.count_nonzero(M)
print("average:", average)

m = len(M)
n = len(M[0])
print("m: ", m)
print("n: ", n)
d = 2

print("M: ", np.shape(M))
# We are initially taking values in U and V such that 
# the entries in M_cap = U*V is close to the average of original matrix M
# we calculate th

#e = np.sqrt(average / 2)
e = 1.0
print("entry :", e)
#U = np.repeat(e, d)
U  = np.array([[e, e]])
print("U :", U)
U = np.repeat(U, m, axis = 0)
print("U :", U)
print("U: ", np.shape(U))

V = np.array([[e, e, e, e, e, e]])
print("V :", V)
V = np.repeat(V, d, axis = 0)
print("V :", V)
print("V: ", np.shape(V))

print("initial M_cap:", np.dot(U, V))

nU, nV = UV_decomposition(M, U, V.T, d)

print("nU :", nU, " ", np.shape(nU))
print("nV :", nV, " ", np.shape(nV))

M_cap = np.dot(nU, (nV.T))
print(M_cap)

print(np.shape(M))


