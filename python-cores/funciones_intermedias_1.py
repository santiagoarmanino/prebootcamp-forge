
# 1- Actualizar valores

matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431


# 2- iterar diccionario

def iterarDiccionario(lista):
    for dic in lista:
        linea = []
        for clave, valor in diccionario.items():
            linea.append(f"{clave} - {valor}")
        print(", ".join(linea))

cantantes2 = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes2)


# 3- iterar diccionario 2

def iterarDiccionario2(llave, lista):
    for dic in lista:
        # verificacion opcional que si estamos seguros de la existencia de la llave, podríamos evitar.
        if llave in dic:
            print(dic[llave])
        else:
            print(f"Error: la llave '{llave}' no esta en el diccionario.")

iterarDiccionario2("nombre", cantantes2)
iterarDiccionario2("pais", cantantes2)


# 4- imprimir informacion

def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}") #A Pesar de que no está pedido explicitamente el pasaje a mayusculas, se agrego porque asi se ve en el ejemplo provisto el output esperado
        for elemento in lista:
            print(elemento)
        print()

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)