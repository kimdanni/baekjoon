# -*- coding: utf-8 -*-
"""
근손실
"""

import itertools

N, K = map(int, input().split())
kit = list(map(int, input().split()))
kit = list(itertools.permutations(kit))
per = len(kit)
for i in kit:
  total_weight = 0
  for j in i:
    total_weight = total_weight + j - K
    if(total_weight < 0):
      per -=1
      break

print(per)
