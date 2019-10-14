#Leetcode accepted
#Time Com : O(n)
class Solution:
    def missingNumber(self, nums):
        nums.sort()
        low = 0
        high = len(nums)
        #Checking the base case
        if nums[0] != 0:
            return 0
        #Checking for 2nd base case
        elif(nums[high-1] != high):
            return high
        #Linearly looking for the missing num
        else:
            for i in range(1,len(nums)):
                if nums[i] != nums[i-1]+1:
                    return nums[i-1]+1

obj = Solution()
print(obj.missingNumber([3,0,1]))
print(obj.missingNumber([9,6,4,2,3,5,7,0,1]))
print(obj.missingNumber([3,0,1]))
print(obj.missingNumber([0]))
