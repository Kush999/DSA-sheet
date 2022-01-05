#Longest consecutive subsequence

def findLongestConseqSubseq(arr, N):
        #code here
    if not arr:
        return 0
    arrset=set(arr)
    result=0
    for num in arrset:
        count=1
        if num-1 not in arrset:
            while num+1 in arrset:
                count+=1
                num+=1
            result=max(result,count)
    return result

arr=[2,6,1,9,4,5,3]
N=len(arr)
print(findLongestConseqSubseq(arr, N))