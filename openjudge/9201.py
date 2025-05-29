import bisect
n = int(input())
l = list(map(int, input().split()))
a = []
ans = 0
for i in range(n - 1, -1, -1):
    speed = l[i]
    if a == []:
        a.append(speed)
    else:
        index = bisect.bisect_right(a, speed)
        ans += n - i - 1 - index
        a.insert(index, speed)
print(ans)
