def find_common_elements(lista1, lista2):
    heap1 = set(lista1)
    heap2 = set(lista2)
    common_elements = []

    for elemento in heap1:
        if elemento in heap2:
            common_elements.append(elemento)
    return common_elements

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(lista1, lista2)
print(common_elements)  # Imprime: [4, 5]
