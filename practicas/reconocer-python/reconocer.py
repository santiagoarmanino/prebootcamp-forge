numero1 = 70 # declaración de variable, tipo de dato: numeral (integer)
numero2 = 3.14 # declaración de variable, tipo de dato: numeral (float)
booleano = False # declaración de variable, tipo de dato: boolean
cadena = 'Hola Mundo' # declaración de variable, tipo de dato: string
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] # tipo de dato: compuesto (lista), inicialización
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} # tipo de dato: compuesto (diccionario), inicialización
frutas = ('guayaba', 'fresa', 'papaya') # tipo de dato: compuesto (tupla), inicialización
print(type(frutas)) # revisión de tipo
print(ingredientes_pastel[2]) # lista: accesar valor
ingredientes_pastel.append('Mantequilla') # lista: agregar valor
print(persona['nombre']) # diccionario: accesar valor
persona['nombre'] = 'Kevin' # diccionario: cambiar valor
persona['color_ojos'] = 'cafe' # diccionario: agregar valor
print(frutas[2]) # tupla: accesar valor

if numero1 > 45: # condicional: if
    print("Numero mayor")
else: # condicional: else
    print("Numero menor")

if len(cadena) < 5: # condicional: if, revisión de tamaño
    print("Cadena corta")
elif len(cadena) > 15: # condicional: else if (elif), revisión de tamaño
    print("Cadena larga")
else: # condicional: else
    print("Cadena perfecta")

for x in range(8): # bucle for, fin: 8
    print(x)
for x in range(2,8): # bucle for, inicio: 2, fin: 8
    print(x)
for x in range(2,8,2): # bucle for, inicio: 2, fin: 8, incremento: 2
    print(x)
x = 0 # declaración de variable (inicio de while)
while(x < 8): # bucle while, fin: 8
    print(x)
    x += 1 # bucle while: incremento

ingredientes_pastel.pop() # lista: borrar valor (último)
ingredientes_pastel.pop(1) # lista: borrar valor (índice 1)

print(persona)
persona.pop('color_ojos') # diccionario: borrar valor
print(persona)

for ingrediente in ingredientes_pastel: # bucle for
    if ingrediente == 'Harina':
        continue # bucle for: continue
    print('Después de la primera sentencia')
    if ingrediente == 'Chocolate':
        break # bucle for: break

def imprime_hola_10_veces(): # función
    for numero in range(10):
        print('Hola')

imprime_hola_10_veces() # llamada a función

def imprime_hola_n_veces(n): # función, parámetro
    for numero in range(n):
        print('Hola')

imprime_hola_n_veces(5) # llamada a función, argumento

def imprime_hola_n_o_diez_veces(n = 10): # función, parámetro por defecto
    for numero in range(n):
        print('Hola')

imprime_hola_n_o_diez_veces() # llamada a función
imprime_hola_n_o_diez_veces(5) # llamada a función, argumento


"""
Sección BONUS: comentario de múltiples líneas
"""

# print(numero3) # Error: NameError
# numero3 = 86
# frutas[0] = 'naranja' # Error: TypeError (las tuplas son inmutables)
# print(persona['hobbies']) # Error: KeyError
# print(ingredientes_pastel[11]) # Error: IndexError
#   print(booleano) # Error: IndentationError
# frutas.append('manzana') # Error: AttributeError (la tupla no tiene append)
# frutas.pop(1) # Error: AttributeError (la tupla no tiene pop)