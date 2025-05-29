n = int(input())
l = list(map(int, input().split()))
dp = [1] * n
dp[-1] = 1
for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if l[i] >= l[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))