# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:02:07 2019

@author: tomsa
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm



def trajplot(f,bounds,p_store,f_store):
    '''INPUTS:
        f : function for plot(used for contour)
        bounds :bounds over which contour is produced
        p_store : trajectory of points 
        f_store : trajectory of function value
    OUTPUTS: 
        contour=True: outputs a contour of function
        below trajectory plot
        plot of function value against iteration
        plot of trajectory within bounds.
    '''
    p_storeX=[0]*int(len(p_store)) 
    #creates empty array for x values
    p_storeY=[0]*int(len(p_store)) 
    #creates empty array for y values
    for i in range(len(p_store)): #separating x1 and x2 values
        p_storeX[i]=(p_store[i][0])
        p_storeY[i]=(p_store[i][1])
    X1=np.linspace(bounds[0][0],bounds[0][1],75)
    X2=np.linspace(bounds[1][0],bounds[1][1],75)
    x1,x2=np.meshgrid(X1,X2)
    z=f([x1,x2])
    plt.figure()
    colors = cm.afmhot(np.linspace(0, 1, len(p_storeY))) #creating colour array
    for i in range(len(p_storeX)): #plotting each point
        plt.plot(p_storeX[i],p_storeY[i],marker='o', markersize=2.5, color=colors[i])
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.contourf(x1,x2,z,100,cmap='cool')
    plt.colorbar()
    plt.show()
    it=np.linspace(0,len(f_store),len(f_store))
    plt.figure()
    plt.plot(it,f_store)
    plt.xlabel('Iterations')
    plt.ylabel('Function Value')
    plt.show()
    return