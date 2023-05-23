import queue

points = [[3,3],[5,-1],[-2,4]]
k=2

pq=queue.PriorityQueue()
for i in points:
    k1=i[0]^2+i[1]^2
    pq.put((k1,i))
result=[]
for i in range(k):
    result.append(pq.get()[1])
print(result)
