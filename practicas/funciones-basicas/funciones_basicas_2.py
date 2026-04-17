def multiplica_por_2(num):
    resultado = []
    for i in range(num + 1):
        resultado.append(i * 2)
    return resultado

# print(multiplica_por_2(5))

def suma_y_resta(lista):
    suma = lista[0] + lista[1]
    resta = lista[0] - lista[1]
    print(suma)
    return resta

# print(suma_y_resta([5, 4]))

def sumatoria_menos_longitud(lista):
    suma_total = sum(lista)
    longitud_lista = len(lista)
    return suma_total - longitud_lista

# print(sumatoria_menos_longitud([1, 2, 3, 4]))

def valores_multiplicados_segundo(lista):
    print(len(lista))
    
    if len(lista) < 2:
        return []
    
    segundo_valor = lista[1]
    nueva_lista = []
    
    for numero in lista:
        nueva_lista.append(numero * segundo_valor)
        
    return nueva_lista

# print(valores_multiplicados_segundo([1, 3, 5, 7]))
# print(valores_multiplicados_segundo([1]))

def valor_multiplicado_longitud(valor, longitud):
    resultado = []
    #OPCIONAL: si longitud es 0, podria hacerse aca un early return de Resultado como en la funcion anterior, simplemente como buena practica. ya que de igual manera no va a tener nada 
    valor_calculado = valor * longitud
    
    for i in range(longitud):
        resultado.append(valor_calculado)
        
    return resultado

# print(valor_multiplicado_longitud(5, 2))
# print(valor_multiplicado_longitud(7, 5))