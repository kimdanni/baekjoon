# -*- coding: utf-8 -*-
"""
2606 바이러스
"""
import collections

N = int(input())
M = int(input())

node_queue = {i : [] for i in range(1,N+1)}


computer_q = collections.deque()
visited = [0 for i in range(N)]
computer_q.append(1)
   
for i in range(M):
    key, value = map(int, input().split())
    node_queue[key].append(value)
    node_queue[value].append(key)

while computer_q:
    cur_node = computer_q.popleft()
    if visited[cur_node - 1] == 0:
        visited[cur_node - 1] = 1
        computer_q.extend(node_queue[cur_node])
        
print(sum(visited) - 1)
