#Maximum and minimum of an array using minimum number of comparisons

#basic solution

arr = [1000, 11, 445, 1, 330, 3000]
n=len(arr)
'''if n==1:
    print(arr[0],arr[0])
else:
    min_elem=min(arr[0],arr[1])
    max_elem=max(arr[0],arr[1])
    for i in range(2,n):
        if arr[i]<min_elem:
            min_elem=arr[i]
        elif arr[i]>max_elem:
            max_elem=arr[i]
    print(min_elem,max_elem)'''

#efficient solution
if n//2==0:
    mx = max(arr[0],arr[1])
    mn = min(arr[0],arr[1])

else:
    mx=arr[0]
    mn=arr[0]

i=0
while i<n-1:
    if arr[i]<arr[i+1]:
        mx = max(mx, arr[i + 1])
        mn = min(mn, arr[i])
    else:
        mx = max(mx, arr[i])
        mn = min(mn, arr[i + 1])
    i+=2
print(mn,mx)
