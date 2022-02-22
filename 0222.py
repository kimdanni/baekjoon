# -*- coding: utf-8 -*-
"""
DFS BFS
"""

from collections import deque
import sys

def dfs(n):
    print(n,  end=" ")
    visited[n] = 1
    for i in graph[n]:
        if not visited[i]:
            dfs(i)
    
def bfs(n):
    visited[n] = 1
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(v,  end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

if __name__=='__main__':
    num = input().split()
    N, M, V = map(int, num)
    graph = [[] for i in range(N+1)]
    visited = [0] * (N+1)
    
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    for i in range(1, N+1):
        graph[i].sort()
    
    dfs(V)
    print()
    visited = [0] * (N+1)
    
    bfs(V)