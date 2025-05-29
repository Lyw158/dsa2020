def merge_sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, left_count = merge_sort_and_count(arr[:mid])
    right, right_count = merge_sort_and_count(arr[mid:])
    
    merged, split_count = merge_and_count_split_inv(left, right)
    
    return merged, left_count + right_count + split_count

def merge_and_count_split_inv(left, right):
    merged = []
    inv_count = 0
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
            inv_count += len(right) - j
        else:
            merged.append(right[j])
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, inv_count
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
_, inv_count = merge_sort_and_count(arr)
print(inv_count)
