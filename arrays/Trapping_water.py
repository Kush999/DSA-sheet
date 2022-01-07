#Trapping Rain Water

#Naive approach

def trappingWater(arr,n):
        #Code here
    res=0
    for i in range(1,n-1):
        left=arr[i]
        for j in range(i):
            left=max(left,arr[j])
        right=arr[i]
        for k in range(i+1,n):
            right=max(right,arr[k])
        res=res+(min(left,right)-arr[i])
    return res

arr=[7,4,0,9]
n=len(arr)
print(trappingWater(arr,n))