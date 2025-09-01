class Solution(object):
    def distinctAverages(self, nums):
        n = len(nums)
        nums.sort()
        arr = set()
        i = 0
        j = n-1
        count = 0
        while i<j:
            avg = (nums[i]+nums[j])/2.0
            arr.add(avg)
            i+=1
            j-=1
        return len(arr)
        