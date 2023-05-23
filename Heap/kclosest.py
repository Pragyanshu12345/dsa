'''Implementing K closest numbers given N from array and K'''
import heapq

arr = [12, 6, 5, 8, 7, 3, 10]
n, x, k = len(arr), 8, 4
y = []
for i in range(n):
    if arr[i] != x:
        heapq.heappush(y, (-abs(x-arr[i]), arr[i]))
        if len(y) > k:
            heapq.heappop(y)
res = []
print(y)
while len(y) > 0:
    print(heapq.heappop(y)[1])
# print(res[::-1])
