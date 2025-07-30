class Solution(object):
    def maxFrequencyElements(self, nums):
        n = len(nums)
        arr={}
        for i in nums:
            if i in arr:
                arr[i]+=1
            else:
                arr[i]=1
        max_freq = max(arr.values())
        total = 0
        for count in arr.values():
            if count == max_freq:
                total += count 
        return total