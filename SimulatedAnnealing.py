# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:39:35 2019

@author: w06650ts
"""
import numpy as np
import numpy.random as rnd
from PlottingUtility import trajplot
import TestFunctions as tf


def SimulatedAnnealing(bounds,f,temp_it,t,td,plot=False):
    '''
    SHORT DESCRIPTION OF WHAT THE FUNCTION DOES

    INPUTS
    bounds: bounds on the function to be optimized
    d     : dimensions of function
    f     : function to be optimized
    temp_it: iterations per temperature
    t     : initial temperature
    td    : temperature decrease per iteration
    plot : Set to true to display plotting utilities
    


    OUTPUT
    p_best             : optimal point
    p_store (optional) : trajectory of points
    
    '''
    d=len(bounds)
    if d!=2 and plot==True:
        print('Plotting only available for 2 Dimensions!')
        plot=False
    #creates initial guess with dimensions same as specified within bounds
    p_new=[0]*int(d) #creating empty p_new array
    p_best=[0]*int(d) #creating empty p_best array
    #iterating over the dimensions creating a random guess for each dimensions
    #specified bounds
    for i in range(d): 
        p_new[i]=rnd.uniform(bounds[i][0],bounds[i][1]) #random guess
        p_best[i]=p_new[i] #sets initial guess as the best guess
    if plot==True: #if a plot is needed, the variables are set up
        p_store=[] #creating empty p_store
        f_store=[] #creating function store 
    while t>0: #while the temperature is above 0
        for i in range(temp_it): 
            #per temperature iterates temp_it times looking for best guess
            for i in range(d):
                p_new[i]=rnd.uniform(bounds[i][0],bounds[i][1]) #create new guess
            delta=f(p_new)-f(p_best)
            #calculate different between best guess and new guess
            if delta<0: 
            #if there is a decrease in f then accept new guess as best
                for i in range(d):
                    p_best[i]=p_new[i]
            elif np.exp(-delta/t) > rnd.uniform(0,1):
            #sometimes accepting an increase
                for i in range(d):
                    p_best[i]=p_new[i]
        t-=td #decreasing temperature
        if plot==True: #adding p_best for each temperature to p_store
            p_store.append(p_best[:])
            f_store.append(f(p_best))
    func_val=f(p_best) #evaluating function at the 'best'
    if plot==True:
        trajplot(f,bounds,p_store,f_store)
        print('Optimum at:',p_best),print('Function value at Optimum:',func_val)
    if plot==False:
        print('Optimum at:',p_best),print('Function value at Optimum:',func_val)
    return 


SimulatedAnnealing([[-5,5],[-5,5]],tf.Rosenbrock,75,5,0.01,plot=True)




    
