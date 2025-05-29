nums = [0, 0, 1, 3, 4, 4]
target = (nums[-1] + 1) // 2
i, j = 0, len(nums) - 1
while i < j:
    mid = (i + j) // 2
    if nums[mid] > target:
        j = mid
    else:
        i = mid + 1
while 
print(i)
