import heapq
class MaxHeap:
    def __init__(self):
        self.heap = []
    def insert(self, elemento):
        heapq.heappush(self.heap, -elemento)
    def extract_max(self):
        max_element = -heapq.heappop(self.heap)
        return max_element

heap_max = MaxHeap()
heap_max.insert(5)
heap_max.insert(3)
heap_max.insert(8)
max_element = heap_max.extract_max()
print(max_element)  # Imprime: 8