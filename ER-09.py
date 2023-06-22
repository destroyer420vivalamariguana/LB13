import heapq
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __lt__(self, other):
        return self.edad < other.edad

heap_personas = []
heapq.heappush(heap_personas, Persona("Ana", 25))
heapq.heappush(heap_personas, Persona("Juan", 30))
heapq.heappush(heap_personas, Persona("María", 20))

for persona in heap_personas:
    print(persona.nombre, persona.edad)
