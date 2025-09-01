class Solution(object):
    def minimumAverage(self, nums):
        arr = []
        n = len(nums)
        nums.sort()
        i=0
        j=n-1
        while i<j:
            avg =(nums[i]+nums[j])/2.0
            arr.append(avg)
            i+=1
            j-=1
        
        return min(arr)    



       
        