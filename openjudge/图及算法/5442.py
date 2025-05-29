class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return False
        self.parent[rooty] = rootx
        return True

def char_to_index(c):
    return ord(c) - ord('A')

def Kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    totalw = 0
    edgecount = 0
    for edge in edges:
        u, v, w = edge
        if uf.union(u, v):
            totalw += w
            edgecount += 1
            if edgecount == n-1:
                break
    return totalw


n = int(input())
edges = []
for i in range(n-1):
    line = list(input().split(' '))
    u = char_to_index(line[0])
    k = int(line[1])
    for j in range(k):
        v = char_to_index(line[2*j+2])
        w = int(line[2*j+3])
        if u < v:
            edges.append((u, v, w))
print(Kruskal(n, edges))
