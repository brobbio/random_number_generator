#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:51:01 2021

@author: bruno.robbio
"""

#RANDOM NUMBER GENERATOR USING LINEAR CONGRUENTIAL METHOD

import datetime

def linear_congruence(m,a,b,seed):
    '''Generates numbers through linear congruence'''
    while True:
        seed = (a*seed+b)%m
        yield seed

#(current_seconds, current_minutes, current_hour) PROVIDE SOME RANDOMNESS TO THE SEED 
current_seconds = datetime.datetime.now().second
current_minutes = datetime.datetime.now().minute
current_hour = datetime.datetime.now().hour

a = 772369 #SLOPE OF LINEAR FUNCTION
b = 56 #Y-INTERCEPT OF LINEAR FUNCTION
seed = 7723+current_seconds+current_minutes+current_hour #INICIAL VALUE OF SEQUENCE
mersenne = 2**31 - 1 #PRIME BIGGER THAN MAX(A,B)
      
generator = linear_congruence(mersenne, a, b, seed)          
        
def random_generator(m):
    '''Generates integers between 0 and m-1'''
    res = next(generator)
    return res%m

print('Enter a positive integer as upper bound (non-inclusive):')
x =  input()
print('How many numbers do you want?')
p = input()
print('Here you go:')
print([random_generator(int(x)) for i in range(int(p))])
