# QuickSort en Python

### Este es un script de Python que implementa el algoritmo de ordenamiento QuickSort. QuickSort es un algoritmo de ordenamiento muy eficiente que utiliza la técnica de "divide y vencerás". Aquí está cómo funciona:

- Primero, elige un "pivote" de la lista de números que quieres ordenar. En este caso, estamos eligiendo el último número de la lista como nuestro pivote.

- Luego, divide la lista en dos grupos: los números que son menores que el pivote y los números que son mayores que el pivote.

- Ordena estos dos grupos de números por separado, utilizando el mismo proceso de "elegir un pivote, dividir la lista en dos, y ordenar los dos grupos". Esto se hace de manera recursiva, lo que significa que el mismo proceso se repite una y otra vez dentro de cada grupo de números.

- Finalmente, une los números ordenados que son menores que el pivote, el pivote mismo, y los números ordenados que son mayores que el pivote. Esto te da la lista completa ordenada.
