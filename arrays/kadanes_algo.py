#Kadane's Algorithm 

arr=[1,2,3,-2,5]
n=len(arr)
max_so_far=0
max_ending_here=0
for i in range(n):
    max_ending_here+=arr[i]
    if max_ending_here<0:
        max_ending_here=0
    if max_so_far<max_ending_here:
        max_so_far=max_ending_here
print(max_so_far)