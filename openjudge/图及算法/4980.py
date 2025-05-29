import heapq

def bfs(n, m, l):
    for i in range(n):
        for j in range(m):
            if l[i][j] == 'r':
                startx, starty = i, j
                break

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[False] * m for _ in range(n)]
    dist = [[float('inf')] * m for _ in range(n)]
    d = heapq.heapify([(0, startx, starty)])
    dist[startx][starty] = 0
    while d:
        time, x, y = heapq.heappop(d)
        if l[x][y] == 'a':
            return time
        if visited[x][y]: continue
        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if l[nx][ny] == '#':
                    continue
                newtime = time + 1
                if l[nx][ny] == 'x':
                    newtime += 1
                if newtime < dist[nx][ny]:
                    dist[nx][ny] = newtime
                    heapq.heappush(d, (newtime, nx, ny))

    return "Impossible"


s = int(input())
ans = []
for i in range(s):
    l = []
    n, m = map(int, input().split())
    for i in range(n):
        l.append(input().strip())
    ans.append(bfs(n, m, l))

for i in ans:
    print(i)