import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 8)

print(heap)
min_element = heapq.heappop(heap)
print('elemento minimo:',min_element)
print(heap)