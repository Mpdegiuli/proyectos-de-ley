```python
def inorder_traversal(root):
    resultado = []
    
    def traverse(node):
        if node:
            traverse(node.left)
            resultado.append(node.val)
            traverse(node.right)
            
    traverse(root)
    return resultado
```