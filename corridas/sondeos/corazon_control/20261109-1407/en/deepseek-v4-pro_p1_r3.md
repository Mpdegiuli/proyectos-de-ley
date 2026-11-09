def inorder_traversal(root):
    values = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        values.append(node.val)
        dfs(node.right)
    dfs(root)
    return values