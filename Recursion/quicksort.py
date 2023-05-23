def partition(arr,s,e):
    i,j=s,e
    pivot=arr[i]
    while(i<j):
        while(i<e and arr[i]<=pivot):
            i+=1
        while(arr[j]>pivot):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    arr[s],arr[j]=arr[j],arr[s]
    return j
def quicksort(arr, s, e):
    if (s<e):
        h=partition(arr,s,e)
        quicksort(arr,s,h-1)
        quicksort(arr,h+1,e)       


arr=[24, 18, 38, 43, 14, 40, 1, 54]
s, e = 0, len(arr)-1
quicksort(arr, s, e)
print(arr)
