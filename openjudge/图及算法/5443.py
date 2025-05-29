import heapq

def dijkstra(graph, start, end):
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:continue
        for v, weight in graph[u].items():
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    path = []
    curr = end
    if dist[end] == float('inf'):
        return None, float('inf')

    while curr is not None:
        path.append(curr)
        curr = prev[curr]
    path.reverse()

    return path, dist[end]

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    idx = 0
    # 第一部分：地点
    P = int(data[idx])
    idx += 1
    name_to_id = {}
    id_to_name = {}
    for i in range(P):
        name = data[idx].strip()
        name_to_id[name] = i
        id_to_name[i] = name
        idx += 1
    # 第二部分：边
    Q = int(data[idx])
    idx += 1
    graph = {i: {} for i in range(P)}
    for _ in range(Q):
        u_str, v_str, d_str = data[idx].split()
        idx += 1
        u = name_to_id[u_str.strip()]
        v = name_to_id[v_str.strip()]
        d = int(d_str)
        graph[u][v] = d
        graph[v][u] = d  # 无向图
    # 第三部分：查询
    R = int(data[idx])
    idx += 1
    results = []
    for _ in range(R):
        src_name, dest_name = data[idx].split()
        idx += 1
        src = name_to_id.get(src_name.strip())
        dest = name_to_id.get(dest_name.strip())
        if src is None or dest is None:
            results.append("Impossible")
            continue
        path, cost = dijkstra(graph, src, dest, P)
        if path is None:
            results.append("Impossible")
        else:
            output = ""
            for i in range(len(path) - 1):
                u = path[i]
                v = path[i + 1]
                d = graph[u][v]
                output += id_to_name[u] + "->({})->".format(d)
            output += id_to_name[path[-1]]
            results.append(output)

    for res in results:
        print(res)

if __name__ == "__main__":
    main()