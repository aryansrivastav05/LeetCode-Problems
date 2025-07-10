class Solution(object):
    def missingNumber(self, nums):
       n = len(nums)
       totalSum = (n*(n+1))/2
       sum = 0
       for i in range(n):
        sum = sum+nums[i]
       return totalSum-sum    


        