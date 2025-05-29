import sys
from collections import defaultdict
import heapq

def get_time(x1, y1, x2, y2, speed):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 / (speed*1000/60)

def dijkstra(graph, start, end):
    dis = {node: float('inf') for node in graph}
    dis[start] = 0
    q = [(0, start)]
    while q:
        cur_dis, cur_node = heapq.heappop(q)
        if cur_dis > dis[cur_node]:
            continue
        for neighbor, weight in graph[cur_node]:
            new_dis = cur_dis + weight
            if new_dis < dis[neighbor]:
                dis[neighbor] = new_dis
                heapq.heappush(q, (new_dis, neighbor))
    return dis[end]

lines = sys.stdin.read().splitlines()
startx, starty, endx, endy = list(map(int, lines[0].split()))
home = (startx, starty)
school = (endx, endy)
nodes = [home, school]
idx = 1
subway_stops = []
while idx < len(lines):
    temp = []
    l = list(map(int, lines[idx].split()))
    for i in range(0, len(l) - 2, 2):
        nx, ny = int(l[i]), int(l[i + 1])
        temp.append((nx, ny))
        nodes.append((nx, ny))
    subway_stops.append(temp)
    idx += 1
graph = defaultdict(list)
walk_speed = 10
subway_speed = 40

for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        u = nodes[i]
        v = nodes[j]
        walk_time = get_time(u[0], u[1], v[0], v[1], walk_speed)
        graph[u].append((v, walk_time))
        graph[v].append((u, walk_time))
for line in subway_stops:
    for i in range(len(line) - 1):
        u = line[i]
        v = line[i + 1]
        time_u_to_v = get_time(u[0], u[1], v[0], v[1], subway_speed)
        graph[u].append((v, time_u_to_v))
        graph[v].append((u, time_u_to_v))

time = dijkstra(graph, home, school)
print(round(time))