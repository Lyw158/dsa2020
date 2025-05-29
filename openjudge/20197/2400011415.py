n, m = list(map(int, input().split()))

ans = 0
while n > 0 and m > 0:
    if n == m:
        ans += 1
        break
    elif n > m:
        n -= m
    else:
        m -= n
    ans += 1

print(ans)