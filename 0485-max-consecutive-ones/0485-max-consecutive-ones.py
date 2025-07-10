class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        count = 0
        temp = 0
        for i in range(n):
            if nums[i]==1:
                count = count+1
                temp = max(temp,count)
                
            else:
                count = 0
        return temp