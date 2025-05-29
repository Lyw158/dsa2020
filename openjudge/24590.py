n = int(input())
ans = []
for i in range(n):
    ans.append(eval(input()))

for i in ans:
    print(f"{i:.2f}")