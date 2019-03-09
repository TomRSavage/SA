# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:54:22 2019

@author: w06650ts
"""

import numpy as np

'''
Presented here is a number of optimization test functions obtained from:
    
https://www.sfu.ca/~ssurjano/optimization.html

The full list is as follows:
    
    Schwefel
    Ackley
    Eggholder
    Rosenbrock
    Sphere
    Rastrigin
    Styblinski-Tang
    Six-Hump Camel
    Easom
    Cross in Tray

'''

def Schwefel(x):
    '''
    INPUTS
    x : arguments of the function Schwefel
    Output
    f : evaluation of the Schwel function given the inputs
    
    DOMAIN           : [-512,512]
    DIMENSIONS       : any
    GLOBAL MINIMUM   : f(x)=0  x=[420.9687...420.9687] 
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
    
    DOMAIN           : [-32,32]
    DIMENSIONS       : any
    GLOBAL MINIMUM   : f(x)=0 x=[0...0]
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
    
    DOMAIN          :[-512,512]
    DIMENSIONS      :2
    GLOBAL MINIMUM  :f(x)=-959.6407 x=[512,404.2319]
    '''
    a=(-x[1]-47)*np.sin(np.sqrt(np.abs(x[1]+(0.5*x[0])+47)))
    b=x[0]*np.sin(np.abs((x[0]-(x[1]+47))))
    return a-b

def Rosenbrock(X):
    '''INPUTS
    X: arguments of the function Rosenbrock
    OUTPUTS
    f : evaluation of the Rosenbrock function given the inputs
    
    DOMAIN         : Xi is within [-5,10] although can be [-2.048,2.048]
    DIMENSIONS     : any
    GLOBAL MINIMUM : f(x)=0 x=[1,...,1] 
'''
    f = sum( 100.0*(X[i+1]-X[i]**2)**2 + (1-X[i])**2 for i in range(0,len(X)-1) )
    return f

def Sphere(X):
    '''INPUTS
    X: arguments of the Sphere Function
    OUTPUTS
    f : evaluation of the Sphere function given the inputs
    
    DOMAIN         : [-5.12,5.12]
    DIMENSIONS     : any
    GLOBAL MINIMUM : f(x)=0 x=[0,...,0] 
'''
    f=sum(X[i]**2 for i in range(0,len(X)))
    return f

def Rastrigin(X):
    '''INPUTS
    X: arguments of the Rastrigin Function
    OUTPUTS
    f : evaluation of the Rastrigin function given the inputs
    
    DOMAIN         : [-5.12,5.12]
    DIMENSIONS     : any
    GLOBAL MINIMUM : f(x)=0 x=[0,...,0] 
'''
    an=10*len(X)
    f_sum=sum(X[i]**2-(10*np.cos(2*np.pi*X[i]))for i in range(len(X)))
    return an+f_sum
     
    

def StyblinskiTang(X):
    '''INPUTS
    X: arguments of the Styblinski-Tang Function
    OUTPUTS
    f : evaluation of the Styblinski-Tang function given the inputs
    
    DOMAIN         : [-5,5]
    DIMENSIONS     : any
    GLOBAL MINIMUM : f(x)=(-39.166*d) x=[-2.9035,...,-2.9035] 
'''
    f_sum=sum(X[i]**4-16*X[i]**2*5*X[i] for i in range(len(X)))
    return f_sum/2
     
    

def SixHumpCamel(X):
    '''INPUTS
    X: arguments of the Six Hump Camel Function
    OUTPUTS
    f : evaluation of the Six Hump Camel function given the inputs
    
    DOMAIN         : X1=[-3,3] X2=[-2,2]
    DIMENSIONS     : 2
    GLOBAL MINIMUM : f(x)=-1.0316 x=[-0.0898,0.7126] 
'''
    a=X[0]**2
    b=X[1]**2
    c=X[0]**4
    d=((4-(2.1*a)+(c/3))*a)+(X[0]*X[1])+((-4+(4*b))*b)
    return d
       
    


def Easom(X):
    '''INPUTS
    X: arguments of the Easom Function
    OUTPUTS
    f : evaluation of the Easom function given the inputs
    
    DOMAIN         : X=[-100,100]
    DIMENSIONS     : 2
    GLOBAL MINIMUM : f(x)=-1 x=[pi,pi] 
'''
    return -np.cos(X[0])*np.cos(X[1])*np.exp(-(X[0]-np.pi)**2-(X[1]-np.pi)**2)
     
    


def CrossInTray(X):
    '''INPUTS
    X: arguments of the Cross in Tray Function
    OUTPUTS
    f : evaluation of the Cross in Tray function given the inputs
    
    DOMAIN         : X=[-10,10]
    DIMENSIONS     : 2
    GLOBAL MINIMUM : f(x)=-2.0626
    
    x=[1.3491,1.3491] 
    x=[-1.3491,1.3491] 
    x=[1.3491,-1.3491] 
    x=[-1.3491,-1.3491] 
'''
    a=np.sin(X[1])*np.sin(X[0])
    b=np.sqrt((X[0]**2)+(X[1]**2))
    c=np.abs(100-(b/np.pi))
    d=np.exp(c)
    e=np.abs(a*d)+1
    return (e**0.1)*-0.0001
     
    
    