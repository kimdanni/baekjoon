# -*- coding: utf-8 -*-


#N , K = map(int, input())

from collections import deque

N, K = map(int, input().split())

meet_que = deque([])
meet_que.append(N)
cur_pos = N

visited_que = [0]*N*K
visited_que[N] = 1

while meet_que:
    cur_pos = meet_que.popleft()
    if(cur_pos == K):
        print(visited_que[cur_pos]-1)
        break
    for i in [cur_pos + 1, cur_pos - 1, cur_pos * 2]:
        if(0 <= i <= K and not visited_que[i]):
            visited_que[i] = visited_que[cur_pos] + 1
            meet_que.append(i)
                