#Count pairs with given sum 

#naive solution
arr=[1, 5, 7, 1]
n=len(arr)
k=int(input())
count=0
'''for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==k:
            count+=1'''


#efficient solution

unorderedMap={}
for i in range(n):
    if k-arr[i] in unorderedMap:
        count+=unorderedMap[k-arr[i]]

    if arr[i] in unorderedMap:
        unorderedMap[arr[i]]+=1

    else:
        unorderedMap[arr[i]]=1
print(count)

