#Chocolate Distribution Problem

def findMinDiff(A,N,M):
    A.sort()
    if M==0 or N==0:
        return 0
    if N<M:
        return -1
    min_diff=A[N-1]-A[0]
    for i in range(N-M+1):
        min_diff=min(min_diff,A[i+M-1]-A[i])
    return min_diff

A=[3, 4, 1, 9, 56, 7, 9, 12]
N=len(A)
M=int(input())
print(findMinDiff(A,N,M))