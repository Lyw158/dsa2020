from collections import defaultdict, deque
import sys

def char_to_index(c):
    return ord(c) - ord('A')

def topological_sort(n, edges):
    in_degree = [0] * n
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    unique = True  # 是否唯一确定

    while queue:
        if len(queue) > 1:
            unique = False  # 存在多种拓扑序列
        node = queue.popleft()
        result.append(node)
        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)

    if len(result) != n:
        return "cycle"  # 存在环
    elif unique:
        return ''.join(chr(ord('A') + c) for c in result)
    else:
        return "ambiguous"

def main():
    lines = sys.stdin.read().splitlines()
    idx = 0
    results = []

    while True:
        if idx >= len(lines):
            break
        line = lines[idx].strip()
        if not line:
            idx += 1
            continue
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break
        idx += 1

        edges = []
        determined = False
        inconsistency = False
        answer_line = ""

        for i in range(m):
            if idx + i >= len(lines):
                break
            rel = lines[idx + i].strip()
            if len(rel) != 3 or rel[1] != '<':
                continue
            u_char, _, v_char = rel
            u = char_to_index(u_char)
            v = char_to_index(v_char)
            edges.append((u, v))
            res = topological_sort(n, edges)
            if res == "cycle":
                results.append(f"Inconsistency found after {i+1} relations.")
                inconsistency = True
                break
            elif res != "ambiguous":
                results.append(f"Sorted sequence determined after {i+1} relations: {res}.")
                determined = True
                answer_line = res
                break

        if not determined and not inconsistency:
            results.append("Sorted sequence cannot be determined.")

        idx += m

    for res in results:
        print(res)

if __name__ == "__main__":
    main()