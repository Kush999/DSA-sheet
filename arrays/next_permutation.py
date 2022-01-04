#Next Permutation

nums = [1,2,3]
n=len(nums)

def nextPermutation(nums,n):

    #Find Pivot Element
    pivot=0
    for i in range(n-1,0,-1):
        if nums[i-1]<nums[i]:
            pivot=i
            break
    if pivot==0:
        return nums.sort()
    #Find the element greater than pivot from end and swap
    swap=n-1
    while nums[swap]<=nums[pivot-1]:
        swap-=1

    nums[swap],nums[pivot-1]=nums[pivot-1],nums[swap]

    #Reverse all elements from pivot point
    nums[pivot:]=reversed(nums[pivot:])
    return nums
print(nextPermutation(nums,n))

