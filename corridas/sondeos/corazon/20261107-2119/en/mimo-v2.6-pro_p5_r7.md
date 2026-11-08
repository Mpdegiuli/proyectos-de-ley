```python
def inorder(root):
    """Return the list of values of a binary tree in inorder (left, root, right).

    Nodes have attributes `val`, `left`, `right`. Recursive strategy.
    """
    result = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result
```