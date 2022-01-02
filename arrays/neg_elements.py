#Move all negative numbers to beginning and positive to end with constant extra space

#simple solution
arr=[-1, 2, -3, 4, 5, 6, -7, 8, 9]
n=len(arr)
'''j=0
for i in range(n):
    if arr[i]<0:
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        j+=1
print(arr)'''

#better solution
left=0
right=n-1
while left<=right:
    if arr[left]<0 and arr[right]<0:
        left+=1
    elif arr[left]>0 and arr[right]<0:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    elif arr[left]>0 and arr[right]>0:
        right-=1
    else:
        left+=1
        right-=1
print(arr)
