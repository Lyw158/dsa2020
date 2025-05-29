def build_tree(preorder, inorder):
    if not preorder or not inorder: return None
    root = preorder[0]
    root_index = inorder.index(root)
    left = build_tree(preorder[1:root_index+1], inorder[:root_index])
    right = build_tree(preorder[root_index+1:], inorder[root_index+1:])
    return (root, left, right)

def postorder(tree):
    if not tree: return []
    root, left, right = tree
    return postorder(left) + postorder(right) + [root]

def solve(preorder, inorder):
    tree = build_tree(preorder, inorder)
    return ''.join(postorder(tree))

ans = []
while True:
    try:
        preorder, inorder = input().split()
        ans.append(solve(preorder, inorder))
    except EOFError:
        break

for a in ans:
    print(a)