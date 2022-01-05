#Array Subset of another array

def subset_array(arr1,arr2,n,m):
    count=0
    for i in arr2:
        if i in arr1:
            count+=1
    if count==m:
        print("Yes")
    else:
        print("No")

arr1=[11, 1, 13, 21, 3, 7]
arr2=[11, 3, 7, 1, 2]
n=len(arr1)
m=len(arr2)
subset_array(arr1,arr2,n,m)
