n, m = list(map(int, input().split()))
l = list(map(int, input().split()))
a = []
for i in range(m):
    s, i = input().split()
    i = int(i)
    a.append([s, i])
ans = []
temp = 0
for op in a:
    if op[0] == 'C':
        temp = (temp + op[1]) % 65536
    else:
        t = 0
        i = op[1]
        for num in l:
            if ((num + temp) >> i) & 1:
                t += 1
        ans.append(t)
for i in ans:
    print(i)