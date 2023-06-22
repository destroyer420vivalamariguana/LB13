def find_median(list1, list2):
    merged = []
    i, j = 0, 0
    n, m = len(list1), len(list2)
    while i < n and j < m:
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    length = len(merged)
    mid = length // 2
    if length % 2 == 0:
        mediana = (merged[mid - 1] + merged[mid]) / 2
    else:
        mediana = merged[mid]
    return mediana
list1 = [1, 3, 5]
list2 = [2, 4, 6]
mediana = find_median(list1, list2)
print("mediana:",mediana)
