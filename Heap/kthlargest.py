''' Heapq module implementation'''
import heapq
l = [21, 45, 78, 3, 5, 7, 44, 10]
LEN = len(l)
k = 3
heap = []
''' inserting - sign to make max heap'''
for i in range(LEN):
    heapq.heappush(heap, -l[i])
    if len(heap) > k:
        heapq.heappop(heap)
print(-heap[0])
