m, n = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(n + 1):
    dp[0][i] = 1
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if i < j:
            dp[i][j] = dp[i][i]
        else:
            dp[i][j] = dp[i][j - 1] + dp[i - j][j]
print(dp[m][n])