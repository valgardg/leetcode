class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        values = set()
        for i in range(k, len(s)+1):
            values.add(s[i-k:i])
        return len(values) == 2**k
