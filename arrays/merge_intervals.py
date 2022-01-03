#Merge Intervals

arr=[[1,3],[2,6],[8,10],[15,18]]
res=[]
for i in sorted(arr):
    if res and i[0]<=res[-1][1]:
        res[-1][1]=max(res[-1][1],i[1])
    else:
        res.append(i)
print(res)
