def find_leftmost(tree, x):
    if tree[x][0] != -1:
        return find_leftmost(tree, tree[x][0])
    
    else:
        return x

def swap_nodes(tree, parent_map, x, y):
    px = parent_map[x]
    py = parent_map[y]
    if px == py:
        if tree[px][0] == x:
            tree[px] = (y, x)
        else:
            tree[px] = (x, y)
    else:
        if tree[px][0] == x:
            tree[px] = (y, tree[px][1])
        else:
            tree[px] = (tree[px][0], y)

        if tree[py][0] == y:
            tree[py] = (x, tree[py][1])
        else:
            tree[py] = (tree[py][0], x)
    
    parent_map[x], parent_map[y] = py, px

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    ptr = 0
    t = int(data[ptr])
    ptr += 1

    results = []

    for _ in range(t):
        n, m = int(data[ptr]), int(data[ptr + 1])
        ptr += 2

        tree = [(-1, -1)] * n
        parent_map = [-1] * n

        for _ in range(n):
            x = int(data[ptr])
            y = int(data[ptr + 1])
            z = int(data[ptr + 2])
            ptr += 3
            tree[x] = (y, z)
            if y != -1:
                parent_map[y] = x
            if z != -1:
                parent_map[z] = x

        for _ in range(m):
            op_type = int(data[ptr])
            ptr += 1
            if op_type == 1:
                x = int(data[ptr])
                y = int(data[ptr + 1])
                ptr += 2
                swap_nodes(tree, parent_map, x, y)
            elif op_type == 2:
                x = int(data[ptr])
                ptr += 1
                results.append(find_leftmost(tree, x))

    for line in results:
        print(line)

if __name__ == '__main__':
    main()