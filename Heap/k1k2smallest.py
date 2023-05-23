import queue
arr= [47,58,93,43,12,10,17]
k1,k2=3,5
pq = queue.PriorityQueue()
for i in arr:
    pq.put(i)
s=0
for i in range(len(arr)):
    y=pq.get()
    if(i+1==k1 or i+1==k2):
        s+=y
print(s)
