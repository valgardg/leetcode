class Solution(object):
    def minCost(self, n):
        """
        :type n: int
        :rtype: int
        """
        onecount = 0
        totalcost = 0
        for i in range(n-1, 0, -1):
            onecount += 1
            totalcost += i
        return totalcost
