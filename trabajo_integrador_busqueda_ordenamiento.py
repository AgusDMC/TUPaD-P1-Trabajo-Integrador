# Algoritmo de ordenamiento: Insertion Sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and actual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual

# Algoritmo de búsqueda: Búsqueda Binaria
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Lista de prueba
numeros = [42, 7, 19, 3, 25, 18, 12]
print("Lista original:", numeros)

# Ordenar la lista
insertion_sort(numeros)
print("Lista ordenada:", numeros)

# Buscar un número
numero_a_buscar = 19
posicion = busqueda_binaria(numeros, numero_a_buscar)

# Mostrar resultados
if posicion != -1:
    print(f"El número {numero_a_buscar} se encuentra en la posición {posicion}.")
else:
    print(f"El número {numero_a_buscar} no se encuentra en la lista.")
