# and, or, not

gas = False
encendido = False
edad = 18

if gas and encendido:
    print("puedes avanzar")

if gas or encendido:
    print("Algo fallo")

if not gas or not encendido:
    print("TODO fallo")

# Operador de Corto circuito. Si la condición de la izquierda esta mal, falla.
if not gas and encendido and edad > 17:
    print("Puedes avanzar")
