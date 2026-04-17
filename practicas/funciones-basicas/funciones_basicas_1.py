# 1.
def cantidad_de_vocales():
    return 5
print(cantidad_de_vocales()) # output: 5

#2
def cantidad_de_glaciares_argentina():
    return 16968
print(cantidad_de_dias_o_meses_o_semanas_en_anio() + cantidad_de_glaciares_argentina())
# output: error consola porque no esta definida la primera funcion.

# 3. 
def anio_independencia_chile():
    return 1810
    return 1851
print(anio_independencia_chile()) #output: 1810

# 4.
def cantidad_de_departamentos_colombia():
    return(32)
    print(33) 
print(cantidad_de_departamentos_colombia()) #output: 32

# 5.
def altura_machu_picchu():
    print(2438) # output: 2438
x = altura_machu_picchu()
print(x) # output: none (le falta return a esa funcion x)

#6
def suma(a, b):
    print(a+b)
print(suma(10, 5) + suma(4, 3)) #output 15, 7 pero luego error al intentar sumar los none que se generan por falta de return

# 7. 
def concatenar(a, b):
    return str(b) + str(a)
print(concatenar(7, 15)) # output: 157 (string)

# 8.
def paises_latinoamerica_o_lenguas_indigenas():
    a = 560
    print(a)
    if a < 180:
        return 33
    else:
        return 46
    return 21
print(paises_latinoamerica_o_lenguas_indigenas()) # output:  560 y 46

# 9.
def cantidad_de_dias_o_meses_o_semanas_en_anio(a, b):
    if a < b:
        return 365 
    else:
        return 12  
    return 52  
print(cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3)) #output: 365
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4)) #output: 12
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4) + cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3)) #output: 377

# 10.
def sumatoria(a, b):
    return a + b
    return 157
print(sumatoria(3, 4)) #output 7

# 11.
a = 150
print(a) #output: 150
def funcion():
    a = 350 # 
    print(a) #output: 350
print(a) # output: 150
funcion()
print(a) # output: 150.

#EN ORDEN, SUCEDEN ASI: 150, 150, 350, 150

# 12.
a = 150
print(a) #output: 150
def funcion():
    a = 350
    print(a)
    return a
print(a) #output: 150
funcion() #output: 350 
print(a) #output: 150

#EN ORDEN, SUCEDEN ASI: 150, 150, 350, 150 (esta version tiene el return que le faltaba a la anterior, pero al llamarse luego no se guarda en ningun lado entonces imprime lo mismo.)


# 13.
a = 150
print(a) #output: 150
def funcion():
    a = 350
    print(a)
    return a
print(a) #output: 150
a = funcion() #output: 350
print(a) #output: 350

#EN ORDEN, SUCEDEN ASI: 150, 150, 350, 350

# 14.
def funcion1():
    print(3)      # output: 3
    funcion2()    
    print(2)      # output: 2
def funcion2():
    print(1)      # output: 1
funcion1()

#EN ORDEN SUCEDEN ASI: 3, 1, 2

# 15.
def funcion1():
    print(3)      # output: 3
    a = funcion2()
    print(a)      # output: 0
    return 4      
def funcion2():
    print(1)      # output: 1
    return 0  
b = funcion1()    
print(b)          # output: 4

# EN ORDEN SUCEDEN ASI: 3, 1, 0, 4