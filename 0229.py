# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 22:03:15 2022

@author: zing1
"""
M = int(input())
N = int(input())

num_list = []

def isPrime(num):
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True

for i in range(M, N+1):
    if(isPrime(i) == True and i > 1):
        num_list.append(i)
    
num_list.sort()
if (len(num_list) <= 0):
    print(-1)
else:
    print(sum(num_list))
    print(num_list[0])