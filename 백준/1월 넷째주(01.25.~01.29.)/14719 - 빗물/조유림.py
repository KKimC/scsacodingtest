from collections import deque
r,c = map(int,input().split())
blocks= [[0]*c for _ in range(r)]
heights = list(map(int,input().split()))

for j in range(c):
    n = heights.pop(0)
    for i in range(r-1,r-n-1,-1):
        blocks[i][j] = 1

dy = [1,-1]
visited = [[False]*c for _ in range(r)]
answer = 0

def fill_water(x,y):
    global answer

    axis = deque([(x,y)])
    fill,cnt = 1,0 #0개수, 벽의 개수

    while axis:
        x,y = axis.popleft()
        for k in range(2):
            ny = y + dy[k]
            if 0<=x<r and 0<=ny<c and not visited[x][ny]:
                if blocks[x][ny] == 1: #벽은 재사용되어야 하기 때문에..! visited = False
                    cnt += 1
                else: 
                    visited[x][ny] = True
                    fill += 1
                    axis.append((x,ny))
    
    if cnt == 2: answer += fill #양끝이 벽인 경우

for i in range(r):
    for j in range(c):
        if blocks[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True 
            fill_water(i,j)

print(answer)
