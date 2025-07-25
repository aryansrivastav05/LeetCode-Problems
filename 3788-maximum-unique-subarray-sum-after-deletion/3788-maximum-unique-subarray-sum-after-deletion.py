class Solution(object):
    def maxSum(self, nums):
       lst = []
       n = len(nums)
       sum = 0
       pos = False
       for i in range(n):
        if nums[i] >=0:
            pos = True
            if nums[i] not in lst:
                lst.append(nums[i])
       if pos==True:
        for value in lst:
            sum = sum+value
        return sum   
       return max(nums)        