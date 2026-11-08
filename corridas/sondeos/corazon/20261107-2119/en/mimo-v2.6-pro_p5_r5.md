```python
# Recursive strategy
def inorderTraversal(root):
    """Return the list of node values of a binary tree in inorder (left, root, right)."""
    result = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)      # left subtree
        result.append(node.val)  # root
        dfs(node.right)     # right subtree

    dfs(root)
    return result
```