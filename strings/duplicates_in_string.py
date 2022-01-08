#Print all the duplicates in the input string

s="aabbceec"
n=len(s)
p={}
for i in s:
    if i in p:
        p[i]+=1
    else:
        p[i]=1

for i in p:
    print(i,p[i])
    print()