# Ej1. Basico 0 a 100
for i in range(101):
    print(i)


# Ej2. Multiples de 2: 2 a 500
for i in range(2, 501, 2):
    print(i)


# Ej3. Contando vanilla ice
for i in range(1, 101):
    if i % 10 == 0: #podria poner 2 también ya que si es divisible por 10, tambien lo es por 2. pero se eligio 10 por legibilidad
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)


# Ej4. Wow, numero gigante
suma = 0
for i in range(0, 500001, 2):
    suma += i

print(suma)


# EJ5. regresame al 3
for i in range(2024, 0, -3):
    print(i)


# Ej6. contador dinamico
numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)