# LIFO (LAST IN FIRS OUT) Ejemplo Historial de navegación

pila = []
pila.append(1)
pila.append(2)
pila.append(3)

print(pila)

ultimoElemento = pila.pop()
print(ultimoElemento)
print(pila)
print(pila[-1])
pila.pop()
pila.pop()
if not pila:
    print("Pila vacia")
