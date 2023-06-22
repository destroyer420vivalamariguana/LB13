import heapq
def heap_sort(lista):
    heap = []
    for elemento in lista:
        heapq.heappush(heap, elemento)
    lista_ordenada = []
    while heap:
        lista_ordenada.append(heapq.heappop(heap))
    return lista_ordenada

lista_desordenada = [9, 5, 2, 7, 1, 6]
lista_ordenada = heap_sort(lista_desordenada)
print(lista_ordenada)  # Imprime: [1, 2, 5, 6, 7, 9]
