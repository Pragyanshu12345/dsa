def bubble(arr, idx):
    if (idx ==n):
        return
    else:
        for i in range(1, n-idx):
            if (arr[i] < arr[i-1]):
                arr[i-1], arr[i] = arr[i], arr[i-1]
        bubble(arr, idx+1)


arr = [4, 67, 3, 31, 2, 66, 10, 5]
idx = 0
n = len(arr)
bubble(arr, idx)
print(arr)
