# -*- coding: utf-8 -*-
"""
12865 평범한 배낭
"""

N, K =  map(int, input().split())

dp = {0 : 0}

for i in range(N):
    tmp = {}
    cur_w, cur_v = map(int, input().split())
    
    for w, v in dp.items():
        if(w + cur_w <= K):
            tmp[w + cur_w] = max(dp.get(w+cur_w,0), v+cur_v)
    dp.update(tmp)
    
print(max(dp.values()))