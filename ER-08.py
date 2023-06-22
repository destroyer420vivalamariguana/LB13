import heapq
def find_k_most_frequent_elements(elements, k):
    frequency = {}
    for elemento in elements:
        frequency[elemento] = frequency.get(elemento, 0) + 1
    heap = []
    for key, value in frequency.items():
        heapq.heappush(heap, (-value, key))
    k_most_frequent = []
    for _ in range(k):
        k_most_frequent.append(heapq.heappop(heap)[1])
    return k_most_frequent

elements = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
k_most_frequent = find_k_most_frequent_elements(elements, 2)
print(k_most_frequent)  # Imprime: [4, 3]
