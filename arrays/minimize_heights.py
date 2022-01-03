#Minimize the Heights II 

arr=[3,9,12,16,20]
k=3
n=len(arr)
arr.sort()
ans=arr[n-1]-arr[0]
smallest=arr[0]+k
largest=arr[n-1]-k
for i in range(n-1):
    mi=min(smallest,arr[i+1]-k)
    mx=max(largest,arr[i]+k)
    if mi<0:
        continue
    ans=min(ans,mx-mi)

print(ans)