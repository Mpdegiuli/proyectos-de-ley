```python
def inorder_traversal(root):
    def walk(node, out):
        if node is None:
            return out
        walk(node.left, out)
        out.append(node.val)
        walk(node.right, out)
        return out

    return walk(root, [])
```