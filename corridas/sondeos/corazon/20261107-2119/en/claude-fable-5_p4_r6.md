```python
# Strategy chosen: recursive
def inorder_traversal(root):
    result = []
    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
    traverse(root)
    return result
```

(Note: no actual image was attached to your message—only a text description of a red heart—so the strategy choice was made arbitrarily rather than based on image content.)