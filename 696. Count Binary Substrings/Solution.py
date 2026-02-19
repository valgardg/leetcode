class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        current = s[0]
        counts = []
        count = 0
        total = 0
        for c in s:
            if c == current:
                count += 1
            else:
                counts.append(count)
                count = 0
                current = c
                count += 1
        if count > 0:
            counts.append(count)
        
        for i in range(1, len(counts)):
            total += min(counts[i], counts[i-1])
        return total

print(Solution().countBinarySubstrings("1100"))
