n = int(input())
poly1, poly2 = [], []
for i in range(n):
    poly1.append(list(map(int, input().split())))
    poly2.append(list(map(int, input().split())))
def add(poly1, poly2):
    ans = []
    poly = {}
    i = 0
    while i < len(poly1):
        poly[poly1[i + 1]] = poly1[i]
        i += 2
    j = 0
    while j < len(poly2):
        if poly2[j + 1] in poly.keys():
            poly[poly2[j + 1]] += poly2[j]
        else:
            poly[poly2[j + 1]] = poly2[j]
        j += 2
    for i in sorted(poly.keys(), reverse=True):
        if poly[i] == 0: continue
        ans.append('[ ' + str(poly[i]) + ' ' + str(i) + ' ]')

    return ans

for p1, p2 in zip(poly1, poly2):
    print(' '.join(add(p1, p2)))
