R = int(input().strip())
N = int(input().strip())
rectangles = [tuple(map(int, input().strip().split())) for _ in range(N)]

def cal_s(k):
    area = 0
    for L, T, W, H in rectangles:
        if L + W <= k:
            area += W * H
        elif L <= k <= L + W:
            area += (k - L) * H
    return area
r = max([t[0] + t[2] for t in rectangles])
l = min([t[0] for t in rectangles])
areasum = cal_s(R)
if r - l == 1:
    print(R)
    exit()
i, j = 0, R
while i < j:
    mid = (i + j) // 2
    if cal_s(mid) >= (areasum + 1) // 2:
        j = mid
    else:
        i = mid + 1
target = cal_s(i)
i, j = 0, R
while i < j:
    mid = (i + j) // 2
    if cal_s(mid) > target:
        j = mid
    else:
        i = mid + 1
print(i - 1)