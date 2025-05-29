class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def preorder(root, res):
    if root:
        res.append(str(root.val))
        preorder(root.left, res)
        preorder(root.right, res)

def main():
    import sys
    line = sys.stdin.readline().strip()
    l = list(map(int, line.split()))
    nums = []
    for num in l:
        if num in nums:
            continue
        nums.append(num)
    if not nums:
        print()
        return
    root = None
    for num in nums:
        if not root:
            root = Node(num)
        else:
            insert(root, num)
    res = []
    preorder(root, res)
    print(' '.join(res))

if __name__ == "__main__":
    main()