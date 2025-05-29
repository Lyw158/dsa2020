n, k = list(map(int, input().split()))
l = list(range(1, n + 1))
kill = []
index = 0
while len(l) > 1:
    index = (index + k - 1) % len(l)
    kill.append(l.pop(index))
print(' '.join(map(str, kill)))