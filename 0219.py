# -*- coding: utf-8 -*-
"""
9012 괄호
"""
from collections import deque

def solution(vps_string):
    deq = deque()
    for i in vps_string:
        if(deq):
            if(deq[-1] == "(" and i ==")"):
                    deq.pop()
                    continue
        deq.append(i)
    if(not deq):
        print("YES")
    else:
        print("NO")

num = int(input(""))
VPS_list = []
for i in range(num):
    VPS = input("")
    VPS_list.append(VPS)
    
for i in VPS_list:
    solution(i)

