def binsearch(arr, s, e, key):
    if (s > e):
        return False
    else:
        mid = (s+e)//2
        if (arr[mid] == key):
            return True
        elif (arr[mid] > key):
            return binsearch(arr, s, mid-1, key)
        else:
            return binsearch(arr, mid+1, e, key)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s, e = 0, len(arr)-1
key = 6
print(binsearch(arr, s, e, key))
