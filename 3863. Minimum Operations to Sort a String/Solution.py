class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        sortedstring = "".join(sorted(s))
        if sortedstring == s:
            return 0
        if len(s) < 3:
            return -1
        
        minc = sortedstring[0]
        maxc = sortedstring[-1]

        if s[0] == minc or s[-1] == maxc:
            return 1
        
        if minc not in s[:-1] and maxc not in s[1:]:
            return 3

        return 2
