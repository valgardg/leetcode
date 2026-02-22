class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        binstr = str(bin(n))[2:]
        if binstr.count("1") < 2:
            return 0
        longest = 0
        last_i = 0

        for i, c in enumerate(binstr):
            if c == "1":
                longest = max(longest, i - last_i)
                last_i = i
            
        return longest
