import heapq
class CustomPriorityHeap:
    def __init__(self):
        self.heap = []
    def insert(self, elemento, prioridad):
        heapq.heappush(self.heap, (-prioridad, elemento))
    def extract_max(self):
        _, max_element = heapq.heappop(self.heap)
        return max_element

heap_prioridad = CustomPriorityHeap()
heap_prioridad.insert("Tarea 1", 2)
heap_prioridad.insert("Tarea 2", 1)
heap_prioridad.insert("Tarea 3", 3)
max_element = heap_prioridad.extract_max()
print(max_element)  # Imprime: "Tarea 3"
