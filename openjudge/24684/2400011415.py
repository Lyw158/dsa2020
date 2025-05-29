l = list(map(int, input().split()))
d = {}

for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
m = max(d.values())
p = [k for k, v in d.items() if v == m]
p.sort()
for i in p:
    print(i, end=' ')