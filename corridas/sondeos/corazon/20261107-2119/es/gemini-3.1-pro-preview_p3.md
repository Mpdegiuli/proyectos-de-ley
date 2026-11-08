```python
def obtener_inorder(root):
    resultado = []
    
    def recorrido_recursivo(nodo):
        if nodo:
            recorrido_recursivo(nodo.left)
            resultado.append(nodo.val)
            recorrido_recursivo(nodo.right)
            
    recorrido_recursivo(root)
    return resultado
```