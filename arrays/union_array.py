#Union of two arrays 
a=[1,2,3,4,5]
b=[1,2,3]
arr=[]
n=len(a)
m=len(b)
if n>m:
    for i in set(a):
        arr.append(i)
    for j in set(b):
        if j not in arr:
            arr.append(j)
else:
    for i in set(b):
        arr.append(i)
    for j in set(a):
        if j not in arr:
            arr.append(j)
print(len(arr))
