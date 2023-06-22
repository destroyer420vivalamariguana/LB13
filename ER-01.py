import heapq
def find_largest_elements(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > 3:
            heapq.heappop(heap)
    return heap
lista_numeros = [12, 54, 23, 67, 45, 9, 41, 73]
largest_elements = find_largest_elements(lista_numeros)
print(largest_elements)  
