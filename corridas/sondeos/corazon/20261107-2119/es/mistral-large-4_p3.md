```python
def inorder(root):
    res = []
    def walk(n):
        if not n:
            return
        walk(n.left)
        res.append(n.val)
        walk(n.right)
    walk(root)
    return res
```