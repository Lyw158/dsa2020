l = []
while True:
    m, n = list(map(int, input().split()))
    if m == 0 and n == 0:
        break
    l.append([m, n])

def count_nodes(m, n):
    i = 0
    cur = m
    ans = 0
    while cur <= n:
        if 2 * cur <= n:
            cur *= 2
            ans += 2 ** i
            i += 1
        else:
            ans += min(2**i, n - cur + 1)
            break
    return ans
for m, n in l:
    print(count_nodes(m, n))