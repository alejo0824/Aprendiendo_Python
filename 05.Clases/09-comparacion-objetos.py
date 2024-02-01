class Coordenadas:
    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon

    # Retornamos TRUE si los argumentos son iguales
    def __eq__(self, otro) -> bool:
        return self.lat == otro.lat and self.lon == otro.lon

    # Función mágica no equal, no iguales, imprime True si son DIFERENTES
    def __ne__(self, otro) -> bool:
        return self.lat != otro.lat or self.lon != otro.lon

    # Menor que. True si efectivamente es menor
    def __lt__(self, otro) -> bool:
        return self.lat + self.lon < otro.lat + otro.lon

    # Menor o igual
    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon


coords = Coordenadas(44, 27)
coords2 = Coordenadas(45, 27)
coords3 = Coordenadas(45, 27)

# Imprime FALSE, porque cuando imprimimos el objeto, imprime el espacio de memoria RAM
# se debe declara la funciónmágica <<__eq__>> para que imprima True si los argumentos de
# dos objetos son iguales o <<__eq__>> imprime True si son DIFERENTES
print(coords != coords2)  # Para la funcion __ne__
print(coords == coords2)  # Para la funcion __eq__

# Otras funciones son menor <<__lt__>>
print(coords < coords3)
print(coords <= coords3)
