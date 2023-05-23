''' Heapq module implementation'''
import heapq
l = [6, 5, 3, 2, 8, 10, 9]
k = 3
heap = []
y = []
''' it automatically implements  min heap '''
for i in l:
    heapq.heappush(heap, i)
    if (len(heap) > k):
        y.append(heapq.heappop(heap))
while (len(heap) != 0):
    y.append(heapq.heappop(heap))
print(y)
