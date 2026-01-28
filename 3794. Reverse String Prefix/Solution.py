class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        prefix = s[:k]
        reversed_prefix = prefix[::-1]
        final_s = reversed_prefix + s[k:]
        return final_s
        
