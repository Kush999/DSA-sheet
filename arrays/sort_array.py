#Sort an array of 0s, 1s and 2s

arr=[0,2,1,2,0]
n=len(arr)
l=0
m=0
h=n-1
while m<=h:
    if arr[m]==0:
        arr[l],arr[m]=arr[m],arr[l]
        l+=1
        m+=1
    elif arr[m]==1:
        m+=1
    else:
        arr[m],arr[h]=arr[h],arr[m]
        m+=1
        h-=1
print(arr)
