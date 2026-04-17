# 1. TAREA: Imprime "Hola, mundo"
print("Hola, mundo")

# 2. Imprime "Hola, Valeria" con el nombre en una variable
nombre = "Valeria"
print("Hola,", nombre) # con una coma 
print("Hola, " + nombre) # con un + 

# 3. Imprimir "Hola 156!" con el número en una variable
numero = 156
print("Hola", numero, "!") # con una coma
# Bonus ninja, corregido del error Typeerror de arriba usando conversión str()
print("Hola " + str(numero) + "!") # con un + 

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables
comida1 = "tacos"
comida2 = "arepas"
print("¡Me encanta comer {} y {}!".format(comida1, comida2)) # con .format()
print(f"¡Me encanta comer {comida1} y {comida2}!") # con cadena f

# Bonus ninja de otros métodos de cadena
texto_ejemplo = "hola, soy santi"
print(texto_ejemplo.upper()) # pasa a mayusculas todo
print(texto_ejemplo.title()) # mayuscula a primera letra d cada palabra
print(texto_ejemplo.replace("santi", "david")) # reemplaza