import heapq
def merge_heaps(heap1, heap2):
    merged_heap = heap1 + heap2
    heapq.heapify(merged_heap)
    return merged_heap
heap1 = [2, 5, 8]
heap2 = [3, 6, 9]
merged_heap = merge_heaps(heap1, heap2)
print(merged_heap) # Imprime: [2, 3, 5, 6, 8, 9]