t, m = list(map(int, input().split()))
l = []
for i in range(m):
    l.append(list(map(int, input().split())))
dp = [0 for i in range(t + 1)]
for i in range(m):
    for j in range(t, l[i][0] - 1, -1):
        dp[j] = max(dp[j], dp[j - l[i][0]] + l[i][1])
print(dp[t])