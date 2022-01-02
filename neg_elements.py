#Move all negative numbers to beginning and positive to end with constant extra space

arr=[-1, 2, -3, 4, 5, 6, -7, 8, 9]
n=len(arr)
j=0
for i in range(n):
    if arr[i]<0:
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        j+=1
print(arr)