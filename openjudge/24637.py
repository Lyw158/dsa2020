n = int(input())
val = list(map(int, input().split()))
dp = [[0, 0] for _ in range(n + 1)]

for i in range(n, 0, -1):
    if 2 * i > n:
        dp[i][0] = 0
        dp[i][1] = val[i - 1]
    else:
        if 2*i + 1 > n:
            dp[i][0] = dp[2*i][1]
            dp[i][1] = val[i - 1]
        else:
            dp[i][0] = max(dp[2*i][0], dp[2*i][1]) + max(dp[2*i+1][0], dp[2*i+1][1])
            dp[i][1] = dp[2 * i][0] + dp[2 * i + 1][0] + val[i - 1]
print(max(dp[1][0], dp[1][1]))