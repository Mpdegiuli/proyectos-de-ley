```python
def inorder_traversal(root):
    def helper(node, result):
        if node is None:
            return result
        helper(node.left, result)
        result.append(node.val)
        helper(node.right, result)
        return result
    
    return helper(root, [])
```