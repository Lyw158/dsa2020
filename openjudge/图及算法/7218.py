from collections import deque

def bfs(l):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    r, c = len(l), len(l[0])
    for i in range(r):
        for j in range(c):
            if l[i][j] == 'S':
                startx, starty = i, j
                break

    visited = [[False] * c for _ in range(r)]
    visited[startx][starty] = True
    d = deque([(startx, starty, 0)])
    while d:
        x, y, time = d.popleft()
        if l[x][y] == 'E':
            return time
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                temp = l[nx][ny]
                if temp == 'E':
                    return time + 1
                elif temp == '.':
                    visited[nx][ny] = True
                    deque.append(d, (nx, ny, time + 1))
    return 'oop!'

t = int(input())
ans = []
for i in range(t):
    r, c = map(int, input().split())
    l = []
    for _ in range(r):
        l.append(list(input().strip()))
    ans.append(bfs(l))
for i in ans:
    print(i)