def sum1(arr, idx,key):
    if idx ==len(arr):
            return False
    else:
        if(arr[idx]==key):
            return True
        return sum1(arr, idx+1,key)


arr = [1, 2, 3,5,6,7,8,9,10]
key=9
idx=0
print(sum1(arr, idx,key))
