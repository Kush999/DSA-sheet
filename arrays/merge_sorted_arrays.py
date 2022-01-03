#Merge Without Extra Space

def merge(arr1,arr2,n,m):
    i=0
    j=0
    k=n-1
    while i<=k and j<m:
        if arr1[i]<arr2[j]:
            i+=1
        else:
            arr2[j],arr1[k]=arr1[k],arr2[j]
            j+=1
            k-=1

    arr1.sort()
    arr2.sort()
    print(arr1)
    print(arr2)

arr1=[1, 3, 5, 7]
arr2=[0, 2, 6, 8, 9]
n=len(arr1)
m=len(arr2)
merge(arr1,arr2,n,m)
