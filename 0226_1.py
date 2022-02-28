# -*- coding: utf-8 -*-
"""
팰린드롬 만들기

"""

from collections import Counter

l = list(input())
perindrom = ["" for i in range(len(l))]
l_dict = [i for i in Counter(l).items()]
l_dict.sort()
iscorrect = 0
midpel = ""
i = 0

for al in l_dict:
    if al[1] % 2 == 1:
        iscorrect += 1
        midpel = al[0]
    for j in range(al[1] // 2):
        perindrom[i] = al[0]
        perindrom[len(l) - i - 1] = al[0]
        i += 1
    if (iscorrect == 1):
        perindrom[len(l) // 2] = midpel
    
    
if iscorrect > 1:
    print("I'm Sorry Hansoo")
else:   
    print(''.join(s for s in perindrom))
