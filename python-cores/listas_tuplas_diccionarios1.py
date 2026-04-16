# 1- carga de datos: 

ventas = [
    {"fecha": "2026-04-10", "producto": "Manaos", "cantidad": 10, "precio": 1.50},
    {"fecha": "2026-04-11", "producto": "Cunnington", "cantidad": 5, "precio": 1.80},
    {"fecha": "2026-04-11", "producto": "Coca-Cola", "cantidad": 3, "precio": 2.50},
    {"fecha": "2026-04-12", "producto": "Manaos", "cantidad": 8, "precio": 1.50},
    {"fecha": "2026-04-12", "producto": "Pepsi", "cantidad": 4, "precio": 2.20},
    {"fecha": "2026-04-13", "producto": "Fanta", "cantidad": 2, "precio": 2.00},
    {"fecha": "2026-04-13", "producto": "Manaos", "cantidad": 12, "precio": 1.40},
    {"fecha": "2026-04-14", "producto": "Cunnington", "cantidad": 6, "precio": 1.80},
    {"fecha": "2026-04-14", "producto": "Sprite", "cantidad": 3, "precio": 2.10},
    {"fecha": "2026-04-15", "producto": "Seven Up", "cantidad": 5, "precio": 2.10}
]

#tanto esta fuente como las variables creadas a partir de ellas en los ejercicios, se usan globalmente puesto que no se especificó en el anunciado modularizar.

# 2- calculo de ingresos totales

ingresos_totales_globales = 0
for venta in ventas:
    ingresos_totales_globales += venta["cantidad"] * venta["precio"]

# 3- Analisis del producto mas vendido 

ventas_por_producto = {}
for venta in ventas:
    prod = venta["producto"]
    cant = venta["cantidad"]
    ventas_por_producto[prod] = ventas_por_producto.get(prod, 0) + cant

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)

# 4- Promedio de precio por producto
precios_por_producto = {}
for venta in ventas:
    prod = venta["producto"]
    ingreso_venta = venta["cantidad"] * venta["precio"]
    if prod not in precios_por_producto:
        precios_por_producto[prod] = [0, 0]
    
    precios_por_producto[prod][0] += ingreso_venta
    precios_por_producto[prod][1] += venta["cantidad"]

promedios_finales = {} 
for prod, datos in precios_por_producto.items():
    promedios_finales[prod] = datos[0] / datos[1] #se podria unpackear para no repetir accesos.
    precios_por_producto[prod] = (datos[0], datos[1]) #(esta linea no es parte del promedio en sí, sino que se aprovecha a pasar de lista a tupla en esta segunda recorrida, para no hacer 3)

# 5- ventas por día 
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    ingresos_por_dia[fecha] = ingresos_por_dia.get(fecha, 0) + ingreso

# 6- representación de datos 
resumen_ventas = {}
for prod in ventas_por_producto: #usamos ventas_por_producto porque es el primero que se volvio "maestro", es decir, que no repite elementos (a diferencia de "ventas"). pero podría haber sido tranquilamente los próximos.
    resumen_ventas[prod] = {
        "cantidad_total": ventas_por_producto[prod],
        "ingresos_totales": precios_por_producto[prod][0],
        "precio_promedio": promedios_finales[prod]
    }


#Entrega final de resultados formateados para consola, de manera que se pueda pasar facilmente a .txt:
print("- RESUMEN FINAL DE VENTAS:")
for producto, info in resumen_ventas.items():
    print(f"Producto: {producto}")
    print(f"  Cantidad total: {info['cantidad_total']}")
    print(f"  Ingresos totales: ${info['ingresos_totales']:.2f}")
    print(f"  Precio promedio: ${info['precio_promedio']:.2f}")
    print("--------------------------")
