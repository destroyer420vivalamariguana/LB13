import heapq
def merge_sorted_lists(listas):
    heap = []
    for i, lista in enumerate(listas):
        if lista:
            heapq.heappush(heap, (lista[0], i, 0))
    merged_list = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        merged_list.append(val)
        if elem_idx + 1 < len(listas[list_idx]):
            heapq.heappush(heap, (listas[list_idx][elem_idx + 1], list_idx, elem_idx + 1))
    return merged_list

lista1 = [1, 4, 7, 10]
lista2 = [2, 5, 6, 8, 11]
lista3 = [3, 9, 12]
listas = [lista1, lista2, lista3]
merged_list = merge_sorted_lists(listas)
print(merged_list)  # Imprime: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
