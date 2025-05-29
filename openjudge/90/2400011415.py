nl, kl, al, bl = [], [], [], []
while True:
    n, k = list(map(int, input().split()))
    if n == 0 and k == 0:
        break
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    nl.append(n)
    kl.append(k)
    al.append(a)
    bl.append(b)

def max_score(n, k, a, b):
    dp = [(0, 0)] * (k + 1)
    for i in range(n):
        for j in range(k, 0, -1):
            if j < i:
                if dp[j - 1][0] * (dp[j][1] + b[i]) > (dp[j][0] + a[i]) * dp[j - 1][1]:
                    dp[j] = dp[j - 1]
                else:
                    dp[j] = (dp[j][0] + a[i], dp[j][1] + b[i])
        dp[0] = (dp[0][0] + a[i], dp[0][1] + b[i])
    return int(100 * max(i[0] / i[1] for i in dp))


for n, k, a, b in zip(nl, kl, al, bl):
    print(max_score(n, k, a, b))