n1 = input("Ingresa primer número: ")
n2 = input("Ingresa segundo número: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
rest = n1 - n2
mult = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numero {n1} y {n2}, 
el resultado de la suma es {suma},
el resultado de la resta es {rest},
el resultado de la division es {div},
el resultado de la multiplicación es {mult},
"""
print(mensaje)
