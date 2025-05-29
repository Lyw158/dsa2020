class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(lines, index=0, depth=0):
    if index >= len(lines):
        return None, index

    current_line = lines[index]
    current_depth = current_line.count('\t')
    line_val = current_line.strip('\t')

    # 当前行不在当前期望的深度，说明没有子节点
    if current_depth != depth:
        return None, index

    node = TreeNode(line_val)
    index += 1

    # 处理左子树
    if index < len(lines):
        next_depth = lines[index].count('\t')
        if next_depth == depth + 1:
            node.left, index = build_tree(lines, index, depth + 1)
        elif next_depth == depth and lines[index].strip('\t') == '*':
            # 空的左子树
            index += 1
            node.right, index = build_tree(lines, index, depth + 1)
        else:
            pass  # 左右子树都为空

    # 处理右子树
    if index < len(lines):
        next_depth = lines[index].count('\t')
        if next_depth == depth + 1:
            node.right, index = build_tree(lines, index, depth + 1)

    return node, index


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

if __name__ == "__main__":
    import sys
    input_text = sys.stdin.read().strip()
    lines = input_text.splitlines()

    root, _ = build_tree(lines)

    print(preorder(root).replace('*', ''))
    print(inorder(root).replace('*', ''))
    print(postorder(root).replace('*', ''))