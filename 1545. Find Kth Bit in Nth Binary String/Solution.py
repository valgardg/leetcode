class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def reverse(w):
            return w[::-1]

        def invert(w):
            return "".join(["1" if c == "0" else "0" for c in w])
        
        s = "0"
        for i in range(n):
            s = s + "1" + reverse(invert(s))
        return s[k-1]
