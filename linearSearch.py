def search(arr, x):

    for i in range(0, len(arr)):
        if (arr[i] == x):
            return f'El elemento esta presente en la posicion {i}'
    return "El elemento no esta presente en la lista"


print(search([1, 5, 2, 8, 23, 51, 56, 9, 24, 51, 63,32, 46, 6], 6))