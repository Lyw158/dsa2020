def can_partition(arr, target_sum):
    total = sum(arr)
    k = total // target_sum
    if k == 0:
        return False
    arr.sort(reverse=True)
    n = len(arr)
    subsets = [0] * k

    def backtrack(index):
        if index == n:
            return all(s == target_sum for s in subsets)
        for i in range(k):
            if i > 0 and subsets[i] == subsets[i-1]:
                continue
            if subsets[i] + arr[index] <= target_sum:
                subsets[i] += arr[index]
                if backtrack(index + 1):
                    return True
                subsets[i] -= arr[index]
        return False

    return backtrack(0)

def find_min_length(sticks):
    total_length = sum(sticks)
    start = max(sticks)
    for i in range(start, total_length + 1):
        if total_length % i == 0:
            if can_partition(sticks, i):
                return i
    
    return total_length
l = []
while True:
    n = int(input())
    if n == 0:
        break
    sticks = list(map(int, input().split()))
    l.append(sticks)
for i in l:
    print(find_min_length(i))