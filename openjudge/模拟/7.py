n, k = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(int(input()))

def numcount(l, k):
    if k == 0:
        return 0
    count = 0
    for i in range(len(l)):
        count += l[i] // k
    return count

l_max = max(l)
ans = 0
i, j = 0, l_max
while i <= j:
    mid = (i + j) // 2
    if numcount(l, mid) >= k:
        ans = mid
        i = mid + 1
    else:
        j = mid - 1
print(ans)