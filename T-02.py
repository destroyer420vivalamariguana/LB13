import heapq
from collections import Counter
def top_k_frequent_words(words, k):
    word_count = Counter(words)
    heap = [(-count, word) for word, count in word_count.items()]
    heapq.heapify(heap)
    top_k = []
    for _ in range(k):
        count, word = heapq.heappop(heap)
        top_k.append(word)
    return top_k
word_list = ['uno', 'uno', 'uno', 'dos', 'tres', 'tres']
k = 2
top_words = top_k_frequent_words(word_list, k)
print(top_words)