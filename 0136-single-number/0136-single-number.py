class Solution(object):
    def singleNumber(self, nums):
        n = len(nums)
        Map = {}
        for i in range(n):
            if nums[i] not in Map:
                Map[nums[i]] = 0
            else:
                Map[nums[i]]+=1
        for num in Map:
            if Map[num]==0:
                return num


