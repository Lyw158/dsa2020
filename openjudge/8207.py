n = int(input())
l = list(map(int, input().split()))
m = int(input())
l = [i for i in l if i <= m]
l.sort()
i, j = 0, len(l) - 1
def find_pair():
    global i, j
    while i < j:
        if l[i] + l[j] == m:
            return i, j
        elif l[i] + l[j] > m:
            j -= 1
        else:
            i += 1
    return False, False
pair = find_pair()
if pair[0] is not False:
    print(l[pair[0]], l[pair[1]])
else:
    print('No')