scores = list(map(float, input().split()))
def count_successful_students(b):
    successful = 0
    for score in scores:
        new_score = b * score + 1.1 ** (b * score / 10 ** 9) * 10 ** 9
        if new_score >= 85 * 10 ** 9:
            successful += 1
    return successful

left, right = 0, 10**9
n = len(scores)
target = int(n * 0.6) + 1
while left < right:
    mid = (left + right) // 2
    if count_successful_students(mid) >= target:
        right = mid
    else:
        left = mid + 1

print(left)