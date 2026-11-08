Utilizo una estrategia recursiva:

```python
def recorrido_en_orden(raiz):
    if raiz is None:
        return []
    return recorrido_en_orden(raiz.left) + [raiz.val] + recorrido_en_orden(raiz.right)
```