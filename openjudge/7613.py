n = int(input())
l = []
for i in range(n):
    l.append(float(input()))
l.sort()
l1 = l[1:-1]
average = sum(l1) / len(l1)
error = max(abs(sample - average) for sample in [l1[0], l1[-1]])
print(f"{average:.2f} {error:.2f}")