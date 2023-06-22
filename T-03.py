import heapq
def find_extremes(names, ages):
    min_heap = [(age, name) for name, age in zip(names, ages)]
    max_heap = [(-age, name) for name, age in zip(names, ages)]
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)

    joven = heapq.heappop(min_heap)[1]
    viejo = heapq.heappop(max_heap)[1]
    return joven, viejo

nombres = ['Miguel', 'Donnel', 'Angel', 'Sebastian']
años = [21, 18, 30, 26]
joven, viejo = find_extremes(nombres, años)
print("El mas joven:", joven)
print("El mas viejo:", viejo)