# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:54:22 2019

@author: w06650ts
"""

import numpy as np



def Schwefel(x):
    '''
    INPUTS
    x : arguments of the function Schwefel
    Output
    f : evaluation of the Schwel function given the inputs
    
    DOMAIN=[-512,512]
    DIMENSIONS= any
    '''
    d=len(x)
    a=418.9829*d
    b=sum(x[i]*np.sin(np.sqrt(np.abs(x[i])))for i in range(d))
    f = a-b
    return f

def Ackley(x):
    '''
    INPUTS
    x : arguments of the function Ackley
    Output
    f : evaluation of the Ackley function given the inputs
    
    DOMAIN=[-32,32]
    DIMENSIONS=2
    '''
    d=len(x)
    a=20
    b=0.2
    c=np.pi*2
    sum1=sum(x[i]**2 for i in range(d))
    sum1=(-a)*np.exp(((-b)*np.sqrt(sum1/d)))
    sum2=sum(np.cos(c*x[i]) for i in range(d))
    sum2=np.exp((sum2/d))
    return sum1-sum2+a+np.exp(1)

def EggHolder(x):
    '''
    INPUTS
    x : arguments of the function Eggholder
    Output
    f : evaluation of the Eggholder function given the inputs
    
    DOMAIN=[-512,512]
    DIMENSIONS=2
    '''
    a=(-x[1]-47)*np.sin(np.sqrt(np.abs(x[1]+(0.5*x[0])+47)))
    b=x[0]*np.sin(np.abs((x[0]-(x[1]+47))))
    return a-b
    