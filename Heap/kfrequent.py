import queue

def k_most_frequent(arr, k):
    # create a dictionary to store the frequency of each element
    freq = {}
    for num in arr:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
    
    # create a min heap to store the k most frequent elements
    pq = queue.PriorityQueue()
    for key, value in freq.items():
        pq.put((-value, key))
    print(pq.qsize())
    # extract the k most frequent elements from the min heap
    result = []
    for i in range(k):
        result.append(pq.get()[1])
    
    return result
arr=[1,1,1,2,2,3,3,3,5,5,5]
print(k_most_frequent(arr,4))
