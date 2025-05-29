class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.left = None
        self.right = None

def build_tree(dfs_sequence):
    root = TreeNode(0)
    stack = [root]
    current_depth = 0
    max_depth = 0
    
    for char in dfs_sequence:
        if char == 'd':
            current_depth += 1
            new_node = TreeNode(current_depth)
            if stack:
                stack[-1].children.append(new_node)
            stack.append(new_node)
            max_depth = max(max_depth, current_depth)
        elif char == 'u':
            stack.pop()
            current_depth -= 1
    
    return root, max_depth

def convert_to_binary_tree(root):
    if not root or not root.children:
        return root, 0
    
    left_child, _ = convert_to_binary_tree(root.children[0])
    prev_sibling = left_child
    for child in root.children[1:]:
        right_child, _ = convert_to_binary_tree(child)
        prev_sibling.right = right_child
        prev_sibling = right_child
    
    root.left = left_child
    root.children = []
    
    return root, 0

def calculate_height(root):
    if not root:
        return 0
    left_height = calculate_height(root.left)
    right_height = calculate_height(root.right)
    return 1 + max(left_height, right_height)

def main():
    dfs_sequence = input().strip()
    original_root, original_height = build_tree(dfs_sequence)
    
    binary_root, _ = convert_to_binary_tree(original_root)
    binary_height = calculate_height(binary_root)
    
    print(f"{original_height} => {binary_height - 1}")

if __name__ == "__main__":
    main()