"""import sys

def main():
    k, n = map(int, sys.stdin.readline().split())
    max_node = (1 << k) - 1

    # Calculate pos using post-order traversal
    current_pos = 0
    pos = [0] * (max_node + 2)  # 1-based indexing

    def post_order(x):
        nonlocal current_pos
        if x > max_node:
            return
        post_order(2 * x)
        post_order(2 * x + 1)
        current_pos += 1
        pos[x] = current_pos

    post_order(1)

    # Calculate start and end for each node
    start = [0] * (max_node + 2)
    end = [0] * (max_node + 2)

    def compute_start(x):
        if x > max_node:
            return
        compute_start(2 * x)
        compute_start(2 * x + 1)
        if 2 * x <= max_node:
            start[x] = start[2 * x]
        else:
            start[x] = pos[x]
        end[x] = pos[x]

    compute_start(1)

    # Segment Tree implementation
    class SegmentTree:
        def __init__(self, size):
            self.n = size
            self.size_tree = 1
            while self.size_tree < self.n:
                self.size_tree <<= 1
            self.tree = [0] * (2 * self.size_tree)
            self.lazy = [0] * (2 * self.size_tree)

        def push(self, node, l, r):
            if self.lazy[node] != 0:
                mid = (l + r) // 2
                # Update left child
                self.tree[2 * node] += self.lazy[node] * (mid - l + 1)
                self.lazy[2 * node] += self.lazy[node]
                # Update right child
                self.tree[2 * node + 1] += self.lazy[node] * (r - mid)
                self.lazy[2 * node + 1] += self.lazy[node]
                # Clear current node's lazy
                self.lazy[node] = 0

        def update_range(self, a, b, val, node, l, r):
            if a > r or b < l:
                return
            if a <= l and r <= b:
                self.tree[node] += val * (r - l + 1)
                self.lazy[node] += val
                return
            self.push(node, l, r)
            mid = (l + r) // 2
            self.update_range(a, b, val, 2 * node, l, mid)
            self.update_range(a, b, val, 2 * node + 1, mid + 1, r)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

        def query_range(self, a, b, node, l, r):
            if a > r or b < l:
                return 0
            if a <= l and r <= b:
                return self.tree[node]
            self.push(node, l, r)
            mid = (l + r) // 2
            left = self.query_range(a, b, 2 * node, l, mid)
            right = self.query_range(a, b, 2 * node + 1, mid + 1, r)
            return left + right

    st = SegmentTree(max_node)

    for _ in range(n):
        parts = sys.stdin.readline().split()
        if parts[0] == '1':
            x = int(parts[1])
            y = int(parts[2])
            l = start[x]
            r = end[x]
            st.update_range(l, r, y, 1, 1, st.size_tree)
        else:
            x = int(parts[1])
            l = start[x]
            r = end[x]
            res = st.query_range(l, r, 1, 1, st.size_tree)
            print(res)

if __name__ == "__main__":
    main()"""
import math
k, n = list(map(int, input().split()))
actions = []
for i in range(n):
    actions.append(list(map(int, input().split())))
total = (1<<k) - 1
tree = [0] * (total + 1)
val = [0] * (total + 1)
lazy = [0] * (total + 1)

def interval(a):
    depth = int(math.log(a, 2))
    len = 2**(k-depth-1)
    return (a-2**depth)*len + 1, (a-2**depth+1)*len

def push_down(node, len):
    lazy[node*2] += lazy[node]
    lazy[node*2+1] += lazy[node]
    tree[node*2] += lazy[node] * (len - 1)
    tree[node*2+1] += lazy[node] * (len - 1)
    val[node*2] += lazy[node]
    val[node*2+1] += lazy[node]
    lazy[node] = 0

def update(l, r, y, p=1, cl=1, cr=2**(k-1)):
    if cl>r or cr<l:
        return
    elif cl>=l and cr<=r:
        val[p] += y
        tree[p] += (2*cl-2*cr+1)*y
        if cr > cl:
            lazy[p] += y
    else:
        mid = (cl+cr)//2
        push_down(p, cr-cl+1)
        update(l, r, y, p*2, cl, mid)
        update(l, r, y, p*2+1, mid+1, cr)
        tree[p] = tree[p*2] + tree[p*2+1] + val[p]

def query(l, r, p=1, cl=1, cr=2**(k-1)):
    if cl>r or cr<l:
        return 0   
    elif cl>=l and cr<=r:
        return tree[p]
    else:
        mid = (cl+cr)//2
        push_down(p, cr-cl+1)
        return query(l, r, p*2, cl, mid) + query(l, r, p*2+1, mid+1, cr) + val[p]

for action in actions:
    l, r = interval(action[1])
    if action[0] == 1:
        update(l, r, action[2])
    else:
        print(query(l, r))
