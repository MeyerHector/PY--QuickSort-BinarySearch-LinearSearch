
def binary_search(list, x):
	low = 0
	high = len(list) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		# Si x es mayor ignora a todos los minors
		if list[mid] < x:
			low = mid + 1

		# Si x es menor ignora a todos los mayores
		elif list[mid] > x:
			high = mid - 1

		# si X se encuentra a la mitad
		else:
			return mid
		
    # EL elemento no se encuentra en la lista
	return -1


list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
x = 7

result = binary_search(list, x)

if result != -1:
	print("EL elemento se encuentra en la posicion ", str(result))
else:
	print("El elemento no se encuentra en el array")
