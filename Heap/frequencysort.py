''' This function is writing the code for frequency sort'''
import queue


def k_most_frequent(arr):
    ''' create a dictionary to store the frequency of each element'''
    freq = {}
    for num in arr:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
    # create a min heap to store the frequent elements
    p_q = queue.PriorityQueue()
    for i in arr:
        p_q.put((-freq[i], i))
    print(p_q.qsize())
    result = []
    for i in range(len(arr)):
        result.append(p_q.get()[1])
    return result


arr = [1, 1, 1, 3, 2, 2, 4, 4]
print(k_most_frequent(arr))
