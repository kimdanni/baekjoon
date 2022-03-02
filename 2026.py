# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 07:43:52 2022

40 :
"""
import sys
from collections import deque

M, N = map(int, input().split())

tomato_box = [list(map(int, input().split())) for i in range(N)]

tomato_que = deque()

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
days = 0

for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 1:
            tomato_que.append([i,j])

def bfs():
    while tomato_que:
        print(tomato_que)
        y, x = tomato_que.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < M and 0 <= ny < N and tomato_box[ny][nx] == 0:
                tomato_box[ny][nx] = tomato_box[y][x] + 1
                tomato_que.append([ny, nx])

bfs()
for i in tomato_box:
    for j in i:
        if j == 0:
            print(-1)
            sys.exit()
    days = max(days, max(i))

print(days - 1)
    
    