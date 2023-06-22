import heapq
def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heapq.heappop(heap)

lista_numeros = [12, 54, 23, 67, 45, 9, 41, 73]
kth_largest = find_kth_largest(lista_numeros, 3)
print(kth_largest)
