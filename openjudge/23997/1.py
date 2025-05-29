n = int(input())
ans = []
path = []
def odd_split(n):
    if n == 0:
        ans.append(path[:])
        return
    if path != [] and n < path[-1] + 2:
        return
    if path == []:
        start = 1
    else:
        start = path[-1] + 2
    for i in range(start, n + 1, 2):
        path.append(i)
        odd_split(n - i)
        path.pop()

odd_split(n)
for i in ans:
    print(' '.join(map(str, i)))
print(len(ans))