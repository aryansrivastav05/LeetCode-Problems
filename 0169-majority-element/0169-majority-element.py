class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        freq = 0
        ans  = 0
        for i in range(n):
            if freq==0:
                ans = nums[i]
              
            if nums[i]==ans:
                  freq=freq+1
            else:
                freq=freq-1
        return ans              



      