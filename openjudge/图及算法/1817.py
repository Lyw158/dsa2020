from collections import deque

m = int(input())
n = int(input())
l = []
for i in range(m):
    l.append(list(map(int, input().split())))
    
visited = [[False for _ in range(n)] for _ in range(m)]

ans = []
def bfs(startx, starty, l):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    d = deque([(startx, starty)])
    size = 1
    while d:
        x, y = d.popleft()
        walls = [(l[x][y] & 8) // 8, (l[x][y] & 4) // 4, (l[x][y] & 2) // 2, l[x][y] & 1]
        for index in range(4):
            if walls[index] == 1:
                continue
            dx, dy = directions[index]
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                d.append((nx, ny))
                size += 1
    return size

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            ans.append(bfs(i, j, l))

print(len(ans))
print(max(ans))