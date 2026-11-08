```python
def recorrido_inorder(root):
    resultado = []
    
    def explorar(nodo):
        if nodo:
            explorar(nodo.left)
            resultado.append(nodo.val)
            explorar(nodo.right)
            
    explorar(root)
    return resultado
```