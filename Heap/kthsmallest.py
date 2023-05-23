''' Heapq module implementation'''
import heapq
l = [21, 45, 78, 3, 5]
k = 3
heap = []
''' it automatically implements min heap '''
heapq.heappush(heap, l[0])
heapq.heappush(heap, l[1])
heapq.heappush(heap, l[2])


# initially added 3 at 4th index then popped 3 which is the smallest

print(heapq.heappushpop(heap, l[3]))
print(heapq.heappop(heap))
print(heapq.nsmallest(k, l))  # returns a list of  k smallest numbers
print(heapq.nlargest(k, l))  # returns a list of  k largest numbers
