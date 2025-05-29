class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(lines):
    stack = []
    root = None
    for line in lines:
        if line == '0':
            break
        dashes = line.count('-')
        val = line[-1]

        node = TreeNode(val)

        while stack and stack[-1][1] >= dashes:
            stack.pop()

        if stack:
            parent_node = stack[-1][0]
            if parent_node.left is None:
                parent_node.left = node
            else:
                parent_node.right = node
        else:
            root = node

        stack.append((node, dashes))

    return root    

def postorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    dfs(root)
    return ''.join(result)

def inorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    dfs(root)
    return ''.join(result)

def preorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ''.join(result)

t = int(input())
ans = []
for _ in range(t):
    lines = []
    while True:
        line = input().strip()
        if line == '0':
            break
        lines.append(line)
    root = build_tree(lines)
    ans.append(preorder(root).replace('*', ''))
    ans.append(postorder(root).replace('*', ''))
    ans.append(inorder(root).replace('*', ''))
    ans.append('')

for a in range(len(ans)-1):
    print(ans[a])