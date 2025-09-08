class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        n = len(nums)
        for i in range(1,n):
            nums[i] = nums[i]+nums[i-1]
        d = {0:1}
        c=0
        for i in range(n):
            extra = nums[i]-goal
            if extra in d:
                c+=d[extra]
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        return c        

        