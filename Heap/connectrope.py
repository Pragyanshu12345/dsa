import queue
rope = [1, 2, 3, 4, 5]
pq = queue.PriorityQueue()
for i in rope:
    pq.put(i)
cost, finalcost = 0, 0
while (pq.qsize() != 1):
    cost = pq.get()+pq.get()
    finalcost += cost
    pq.put(cost)
print(finalcost)
