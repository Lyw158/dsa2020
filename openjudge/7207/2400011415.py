n = int(input())
m = 2 * n - 1
a = [[0] * (2*n - 1) for i in range(2*n - 1)]
a[0][n - 1] = 1
cur = [0, n - 1]
i = 1
while i < (2*n - 1) ** 2:
    if a[(cur[0] - 1 + m) % m][(cur[1] + 1) % m] != 0 or (cur[0] == 0 and cur[1] == m - 1):
        a[(cur[0] + 1) % m][cur[1]] = i + 1
        cur = [(cur[0] + 1) % m, cur[1]]
    else:
        a[(cur[0] - 1  + m) % m][(cur[1] + 1) % m] = i + 1
        cur = [(cur[0] - 1 + m) % m, (cur[1] + 1) % m]
    i += 1
for i in range(m):
    for j in range(m):
        print(a[i][j], end=' ')
    print()