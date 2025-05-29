import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    costs = []
    for _ in range(n):
        costs.append(int(sys.stdin.readline()))
    max_cost = max(costs)
    low = max_cost
    high = sum(costs)
    answer = high  # 初始设为最大可能值
    
    while low <= high:
        mid = (low + high) // 2
        current_sum = 0
        count = 1
        
        for c in costs:
            if current_sum + c > mid:
                count += 1
                current_sum = c
                if count > m:
                    break
            else:
                current_sum += c
        
        if count <= m:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    
    print(answer)

if __name__ == "__main__":
    main()