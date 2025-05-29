n, k = list(map(int, input().split()))
l = []
for i in range(n):
    a, b = list(map(int, input().split()))
    l.append([a, b, i+1])

l.sort(key=lambda x: -x[0])
l1 = l[0:k]
l1.sort(key=lambda x: -x[1])
print(l1[0][2])