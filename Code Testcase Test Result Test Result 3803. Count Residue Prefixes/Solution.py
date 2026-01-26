class Solution(object):
    def residuePrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_valid(prefix):
            return len(set(prefix)) == len(prefix) % 3

        p = ""
        count = 0
        for c in s:
            p += c
            if is_valid(p): count +=1 

        return count
