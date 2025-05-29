n = int(input().strip())
l = []
for _ in range(n):
    i, j = list(map(int, input().split()))
    l.append((i, j))
l.sort(key=lambda x: x[1])
ans = 1
cur = l[0][1]
for i in range(1, len(l)):
    if l[i][0] > cur:
        ans += 1
        cur = l[i][1]
print(ans)