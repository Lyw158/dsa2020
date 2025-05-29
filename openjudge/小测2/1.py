s = list(map(int, input().split()))[:-2]
t = list(map(int, input().split()))[:-2]
sd = {}
td = {}
for i in range(0, len(s), 2):
    sd[s[i + 1]] = s[i]
for j in range(0, len(t), 2):
    td[t[j + 1]] = t[j]

def add(d1, d2):
    for i in d1.keys():
        if i in d2.keys():
            d2[i] = d1[i] + d2[i]
        else:
            d2[i] = d1[i]
    return d2

def mul(d1, d2):
    ans = {}
    for i in d1.keys():
        for j in d2.keys():
            ans[i + j] = ans.get(i + j, 0) + d1[i] * d2[j]
    return ans

a = add(sd, td)
b = mul(sd, td)
for i in sorted(a.keys(), reverse=True):
    if a[i] != 0:
        if a[i] > 0 and i != max(a.keys()):
            if a[i] == 1 and i != 0:
                print(f'+x^{i}', end='')
            elif i == 0:
                print(f'+{a[i]}', end='')
            else:
                print(f'+{a[i]}x^{i}', end='')
        else:
            if a[i] == -1 and i != 0:
                print(f'-x^{i}', end='')
            elif i == 0:
                print(f'{a[i]}', end='')
            else:
                print(f'{a[i]}x^{i}', end='')
print()
for i in sorted(b.keys(), reverse=True):
    if b[i] != 0:
        if b[i] > 0 and i != max(b.keys()):
            if b[i] == 1 and i != 0:
                print(f'+x^{i}', end='')
            elif i == 0:
                print(f'+{b[i]}', end='')
            else:
                print(f'+{b[i]}x^{i}', end='')
        else:
            if b[i] == -1 and i != 0:
                print(f'-x^{i}', end='')
            elif i == 0:
                print(f'{b[i]}', end='')
            else:
                print(f'{b[i]}x^{i}', end='')