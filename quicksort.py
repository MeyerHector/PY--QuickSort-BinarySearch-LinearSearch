import random

def quicksort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[-1]

    menores = []
    for x in lst[:-1]:
        if x < pivot:
            menores.append(x)

    mayores = []
    for x in lst[:-1]:
        if x >= pivot:
            mayores.append(x)

    return quicksort(menores) + [pivot] + quicksort(mayores)

numeros = [random.randint(1, 100) for _ in range(20)]
print('Lista desordenada:')
print(numeros)

print('Lista ordenada')
print(quicksort(numeros))