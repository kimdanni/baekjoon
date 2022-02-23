# -*- coding: utf-8 -*-
"""
2178 미로 탐색
"""

maze = []

N, M = map(int, input().split())

visited = [[0 for i in range(M)]for i in range(N)]

for i in range(N):
    maze.append(list(map(int, input())))

route = [[0,0]]

n_row = 0
n_col = 0
def bfs():
    four_way = [[-1,0], [0,-1], [1,0], [0,1]]
    while route:
        row ,col = route.pop(0)
        if(row == N-1 and col == M-1):
            print(visited[row][col] + 1)
            break
        for i in range(4):
            n_row = row + four_way[i][0]
            n_col = col + four_way[i][1]
            if 0 <= n_row < N and 0 <= n_col < M:
                if (maze[n_row][n_col] == 1 and visited[n_row][n_col] == 0):
                    visited[n_row][n_col] = visited[row][col] + 1
                    route.append([n_row,n_col])
bfs()