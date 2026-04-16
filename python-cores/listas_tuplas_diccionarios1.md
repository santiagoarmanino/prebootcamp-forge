# Informe de análisis de ventas

## Lista de ventas original
Registro crudo de las ventas generadas como ejemplo:

* 2026-04-10 | Manaos | 10 uds | $1.50 c/u
* 2026-04-11 | Cunnington | 5 uds | $1.80 c/u
* 2026-04-11 | Coca-Cola | 3 uds | $2.50 c/u
* 2026-04-12 | Manaos | 8 uds | $1.50 c/u
* 2026-04-12 | Pepsi | 4 uds | $2.20 c/u
* 2026-04-13 | Fanta | 2 uds | $2.00 c/u
* 2026-04-13 | Manaos | 12 uds | $1.40 c/u
* 2026-04-14 | Cunnington | 6 uds | $1.80 c/u
* 2026-04-14 | Sprite | 3 uds | $2.10 c/u
* 2026-04-15 | Seven Up | 5 uds | $2.10 c/u

---

## Ingresos totales generados
La sumatoria de todas las ventas dio bruto total de **$100.70**.

---

## Producto más vendido
El producto mas vendido fue **Manaos**, con una cantidad total vendida de **30 unidades**.

---

## Precio promedio de venta por producto
Ordenado de mayor a menor valor:

* **Coca-Cola:** $2.50
* **Pepsi:** $2.20
* **Sprite:** $2.10
* **Seven Up:** $2.10
* **Fanta:** $2.00
* **Cunnington:** $1.80
* **Manaos:** $1.46

---

## Ingresos totales por dia
Agrupados por fecha de menos recientes a más recientes:

* **2026-04-10:** $15.00
* **2026-04-11:** $16.50
* **2026-04-12:** $20.80
* **2026-04-13:** $20.80
* **2026-04-14:** $17.10
* **2026-04-15:** $10.50

---

## Resumen de ventas por producto
Formateado, el detalle de cantidades, ingresos totales y el precio promedio obtenido de las ventas.

| Producto | Cantidad total | Ingresos totales | Precio promedio |
| :--- | :---: | :---: | :---: |
| **Manaos** | 30 | $43.80 | $1.46 |
| **Cunnington** | 11 | $19.80 | $1.80 |
| **Coca-Cola** | 3 | $7.50 | $2.50 |
| **Pepsi** | 4 | $8.80 | $2.20 |
| **Fanta** | 2 | $4.00 | $2.00 |
| **Sprite** | 3 | $6.30 | $2.10 |
| **Seven Up** | 5 | $10.50 | $2.10 |

---

## Analisis del paso a paso para obtener los resultados:

Para llegar a estos resultados, el script de python se programó procesando los datos con una logica de etapas:

**Estructuracion de datos con diccionarios:** En lugar de usar listas simples, se uso diccionarios porque permiten indexar la información por el nombre del producto, lo cual facilita la búsqueda y evita tener datos duplicados por ahí.
**Acumulaciones usando get:** Durante la lectura de la lista de ventas, utilicé el método .get porque permite centralizar todas las ventas sin excederse de pasadas (ineficientes).
**Calculo de metricas derivadas:** Una vez hecho el "maestro", realicé una segunda iteración para calcular el promedio de venta de cada articulo y aplicar una sobrescritura que pase los datos de lista a tupla que es fija y más segura para el reporte final.
**Consolidado final:** En resumen_ventas, al estar anidados los diccionarios dentro de otros, cada producto tiene ahora su propia pequeña ficha tecnica con toda la info ya masticada y lista para ser presentada en este informe.

---

## Analisis de resultados finales:
* **Producto lider:** El producto con mayor ventas fue **Manaos** con 30 unidades vendidas.
* **Mayor rentabilidad:** **Coca-Cola** tuvo el precio promedio de venta mas alto (producto con mayor precio unitario).

---
