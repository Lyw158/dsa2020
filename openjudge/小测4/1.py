import heapq

def minimum_cost_to_cut_planks(lengths):
    # 将所有木板长度加入最小堆
    heapq.heapify(lengths)
    
    total_cost = 0
    
    # 当堆中还有多于一个木板时继续合并
    while len(lengths) > 1:
        # 取出两个最短的木板
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)
        
        # 合并这两个木板
        merged = first + second
        
        # 记录合并的成本
        total_cost += merged
        
        # 将合并后的木板重新加入堆中
        heapq.heappush(lengths, merged)
    
    return total_cost

# 输入处理
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    lengths = list(map(int, data[1:]))
    
    result = minimum_cost_to_cut_planks(lengths)
    print(result)