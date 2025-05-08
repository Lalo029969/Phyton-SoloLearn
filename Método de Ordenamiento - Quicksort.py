# Programa: Método de Ordenamiento Quicksort en Python

def quicksort(lista):

    """
    Función que implementa el algoritmo de ordenamiento rápido (quicksort).
    
    Parámetros:
    lista (list): Una lista de elementos que se desea ordenar.
    
    Devuelve:
    list: La lista ordenada en orden ascendente.
    """
    
    # Caso base: Si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(lista) <= 1:
        return lista
    
    # Seleccionamos un pivote (usaremos el último elemento como pivote)
    pivote = lista[-1]
    
    # Dividimos la lista en tres partes:
    # 1. Menores: Elementos menores al pivote
    menores = [x for x in lista[:-1] if x <= pivote]
    
    # 2. Mayores: Elementos mayores al pivote
    mayores = [x for x in lista[:-1] if x > pivote]
    
    # 3. El pivote se coloca entre las dos listas tras ordenar
    # Llamamos recursivamente a quicksort para las sublistas
    return quicksort(menores) + [pivote] + quicksort(mayores)

# Lista de ejemplo para ordenar
lista_desordenada = [10, 7, 8, 9, 1, 5]

# Mostramos la lista original
print("Lista original:", lista_desordenada)

# Ordenamos la lista usando quicksort
lista_ordenada = quicksort(lista_desordenada)

# Mostramos la lista ordenada
print("Lista ordenada:", lista_ordenada)


"""

Explicación paso a paso del algoritmo:

1. Caso base:

Si la lista tiene uno o cero elementos (len(lista) <= 1), ya está ordenada, y se devuelve directamente.



2. Elección del pivote:

Seleccionamos un elemento de la lista como pivote. En este ejemplo, tomamos el último elemento (lista[-1]).



3. División de la lista:

Usamos comprensión de listas para separar:

Los elementos menores o iguales al pivote.

Los elementos mayores al pivote.




4. Recursión:

Ordenamos recursivamente las sublistas menores y mayores usando quicksort.

Finalmente, combinamos los resultados: quicksort(menores) + [pivote] + quicksort(mayores).



5. Resultado:

La lista se ordena en orden ascendente.





---

Salida del programa:

Lista original: [10, 7, 8, 9, 1, 5]

Lista ordenada: [1, 5, 7, 8, 9, 10]



---


Complejidad del algoritmo:

 • Mejor y promedio caso: O(n log n), gracias a la división recursiva.
 
  • Peor caso: O(n²), cuando los elementos están muy desbalanceados (por ejemplo, ya ordenados si no optimizamos el pivote).
  
   Es un algoritmo eficiente y ampliamente utilizado en la práctica.



"""

