```python
def inorderTraversal(root):
    resultado = []
    pila = []
    nodo_actual = root
    
    while nodo_actual or pila:
        while nodo_actual:
            pila.append(nodo_actual)
            nodo_actual = nodo_actual.left
            
        nodo_actual = pila.pop()
        resultado.append(nodo_actual.val)
        nodo_actual = nodo_actual.right
        
    return resultado
```