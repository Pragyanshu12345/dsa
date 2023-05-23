def mergesort(arr, s, e):
    if (s >= e):
        return 0
    else:
        k = 0
        mid = (s+e)//2
        k = mergesort(arr, s, mid)+mergesort(arr, mid+1, e)
        k = k+merge(arr, s, mid, e)
        return k


def merge(arr, s, mid, e):
    first = arr[s:mid+1]
    second = arr[mid+1:e+1]
    a, b = len(first), len(second)
    i, j, k = 0, 0, s
    y = 0
    while (i < a and j < b):
        if (first[i] <= second[j]):
            arr[k] = first[i]
            i, k = i+1, k+1
        else:
            arr[k] = second[j]
            j, k = j+1, k+1
            y += (mid-s+1)-i
    while (j < b):
        arr[k] = second[j]
        j, k = j+1, k+1
    while (i < a):
        arr[k] = first[i]
        i, k = i+1, k+1
    del first, second
    return y


arr = [8, 5, 3, 4, 1, 6, 2]
s, e = 0, len(arr)-1
print(mergesort(arr, s, e))
print(arr)
