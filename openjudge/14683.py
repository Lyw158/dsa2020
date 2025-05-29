import heapq

n = int(input())
a = list(map(int, input().split()))
heapq.heapify(a)
total = 0

while len(a) > 1:
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    s = x + y
    total += s
    heapq.heappush(a, s)

print(total)