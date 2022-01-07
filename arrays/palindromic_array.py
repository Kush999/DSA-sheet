#Palindromic Array

def palindromic(arr,n):
    for i  in arr:
        p=str(i)
        b=p[::-1]
        if b!=p:
            return 0
    return 1

arr=[111, 222, 333, 444, 555]
n=len(arr)
print(palindromic(arr,n))