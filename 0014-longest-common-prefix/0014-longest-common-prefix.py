class Solution(object):
    def longestCommonPrefix(self, strs):
        n = len(strs)
        strs.sort()
        s1 = strs[0]
        s2 = strs[n-1]
        result = []
        for i in range(min(len(s1), len(s2))):
            if s1[i]!=s2[i]:
                break
            result.append(s1[i])
        return "".join(result)        

       
            

        
        