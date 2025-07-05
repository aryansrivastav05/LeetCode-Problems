import math
class Solution(object):
    def maxSubArray(self, nums):
        sum = 0
        maxSum = float('-inf')
        n = len(nums)
        for i in range(n):
            sum = sum+nums[i]
            if(sum>maxSum):
                maxSum = sum
            if(sum<0):
                sum = 0 
        return maxSum           
       
        