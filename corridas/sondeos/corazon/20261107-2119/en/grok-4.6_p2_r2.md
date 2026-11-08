def inorderTraversal(root):
    def dfs(node, res):
        if node:
            dfs(node.left, res)
            res.append(node.val)
            dfs(node.right, res)
    res = []
    dfs(root, res)
    return res