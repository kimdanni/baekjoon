# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 19:26:00 2022

@author: zing1
"""
import heapq
import sys

heap = []

process_list = []

N = int(sys.stdin.readline())

for i in range(N):
    process_list.append(int(sys.stdin.readline()))
    
    
for i in process_list:
    if (i == 0):
        if(len(heap) == 0):
            print(0)
        else:
            result = heapq.heappop(heap)
            print(result)
    else:
        heapq.heappush(heap, i)