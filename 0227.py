# -*- coding: utf-8 -*-
"""
설탕 배달
"""

suger = int(input())
bump = 0

while suger > 0:
    if (suger % 5 == 0):
        suger -= 5
        bump += 1
    else:
        suger -= 3
        bump += 1
    
if (suger < 0):
    print(-1)
else:
    print(bump)