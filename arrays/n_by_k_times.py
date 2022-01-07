#Given an array of size n and a number k, find all elements that appear more than n/k times

arr=[3, 1, 2, 2, 1, 2, 3, 3]
n=len(arr)
k=int(input())
ans=n//k
p={}
for i in arr:
    if i in p:
        p[i]+=1
    else:
        p[i]=1
print(p)
for j in p:
    if p[j]>ans:
        print(j, end=" ")