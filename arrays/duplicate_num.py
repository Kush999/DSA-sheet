#Find the Duplicate Number

def findDuplicate(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            return nums[i]
nums=[3,1,3,4,2]
print(findDuplicate(nums))