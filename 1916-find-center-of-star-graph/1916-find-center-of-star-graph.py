class Solution(object):
    def findCenter(self, edges):
        n = len(edges)+1
        lst=[[]for i in range(n+1)]
        for i,j in edges:
            lst[i].append(j)
            lst[j].append(i)
        for i in range(1, n + 1):
            if len(lst[i]) == n - 1:
                return i
        