```python
def inorder(root):
    res = []
    def rec(n):
        if n:
            rec(n.left)
            res.append(n.val)
            rec(n.right)
    rec(root)
    return res
```