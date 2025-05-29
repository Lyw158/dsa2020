from collections import deque
n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().strip())))

def bfs_find(l, start, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque([start])
    island = []
    visited[start[0]][start[1]] = True

    while q:
        x, y = q.popleft()
        island.append((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(l) and 0 <= ny < len(l[0]) and l[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    return island

def bfs_find_bridge(l, island1):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque(island1)
    visited = [[False] * len(l[0]) for _ in range(len(l))]
    for x, y in island1:
        visited[x][y] = True
    steps = 0
    while q:
        size = len(q)
        for _ in range(size):
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(l) and 0 <= ny < len(l[0]) and not visited[nx][ny]:
                    if l[nx][ny] == 1:
                        return steps
                    visited[nx][ny] = True
                    q.append((nx, ny))
        steps += 1
    return -1

def shortest_bridge(l):
    visited = [[False] * len(l[0]) for _ in range(len(l))]
    island1 = []
    found = False
    for i in range(n):
        for j in range(len(l[0])):
            if l[i][j] == 1 and not visited[i][j]:
                island1 = bfs_find(l, (i, j), visited)
                found = True
                break
        if found:
            break
    return bfs_find_bridge(l, island1)

print(shortest_bridge(l))
