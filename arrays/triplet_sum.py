#Triplet Sum in Array

def Find_Triplet(arr,n,x):
    arr.sort()
    for i in range(n):
        sum=X-arr[i]
        j=i+1
        k=n-1
        while j<k:
            if arr[j]+arr[k]<sum:
                j+=1
            elif arr[j]+arr[k]>sum:
                k-=1
            else:
                return 1
    return 0

arr=[1, 4, 45, 6, 10, 8]
n=len(arr)
X=int(input())
print(Find_Triplet(arr,n,X))
