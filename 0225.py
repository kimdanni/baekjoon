# -*- coding: utf-8 -*-
"""
단지번호붙이기
"""
from collections import deque

N = int(input())
map_list = []
for i in range(N):
    map_list.append(list(map(int,list(input()))))

visited = [[0 for i in range(N)] for i in range(N)]

map_total_sum = 0
sum_map_list = []
for i in map_list:
    map_total_sum += sum(i)
house_queue = deque()
# map_list 의 총합과 visited 의 총합이 같아질 때 까지
for i in range(N):
    for j in range(N):
        if (map_list[i][j] == 1 and visited[i][j] == 0):
            visited[i][j] = 1
            house_queue = deque()
            house_queue.append([i,j])
            total_batch_house = 1
            while house_queue:
                mv_pos = [[-1,0],[0,-1],[1,0],[0,1]]
                house_pos = house_queue.popleft()
                for pos in mv_pos:
                    if 0 <= house_pos[0]+pos[0] < N and 0 <= house_pos[1]+pos[1] < len(map_list):
                        if (map_list[house_pos[0]+pos[0]][house_pos[1]+pos[1]] == 1 and visited[house_pos[0]+pos[0]][house_pos[1]+pos[1]] == 0):
                            house_queue.append([house_pos[0]+pos[0],house_pos[1]+pos[1]])
                            total_batch_house += 1
                            visited[house_pos[0]+pos[0]][house_pos[1]+pos[1]] = total_batch_house
            sum_map_list.append(total_batch_house)
sum_map_list.sort()
print(len(sum_map_list))

for i in range(0, len(sum_map_list)):
    print(sum_map_list[i])
    
