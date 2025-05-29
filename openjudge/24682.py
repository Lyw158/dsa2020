from collections import deque

n, r = list(map(int, input().split()))
edges = [[] for i in range(n+1)]
for i in range(n-1):
    u, v = list(map(int, input().split()))
    edges[u].append(v)
    edges[v].append(u)

Q = int(input())
query = []
for i in range(Q):
    query.append(list(map(int, input().split())))
parent = [0] * (n + 1)
depth = [0] * (n + 1)
visited = [False] * (n+1)
q = deque()
q.append(r)
visited[r] = True
parent[r] = 0
while q:
    u = q.popleft()
    for v in edges[u]:
        if not visited[v] and v != parent[u]:
            visited[v] = True
            depth[v] = depth[u] + 1
            parent[v] = u
            q.append(v)

for i in range(Q):
    u, v = query[i]
    while depth[u] > depth[v]:
        u = parent[u]
    while depth[u] < depth[v]:
        v = parent[v]
    while u != v:
        u = parent[u]
        v = parent[v]
    print(u)