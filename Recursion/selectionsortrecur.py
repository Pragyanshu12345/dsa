def selection(arr, idx):
    if (idx ==n):
        return
    else:
        mini=arr[idx]
        temp=idx
        for i in range(idx,n):
            if (mini>arr[i]):
                mini=arr[i]
                temp=i
        arr[idx],arr[temp]=arr[temp],arr[idx]
        selection(arr, idx+1)


arr = [3243,34,545,323,434,232,1,3,4,5,33]
idx = 0
n = len(arr)
selection(arr, idx)
print(arr)