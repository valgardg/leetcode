import math

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ''
        
        gcd_len = math.gcd(len(str1), len(str2))
        return str1[:gcd_len]

    def solve(self):
        print(self.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
        print(self.gcdOfStrings("ABABABAB", "ABAB"))
        print(self.gcdOfStrings("AAAAAA", "AACC"))
solution = Solution()
solution.solve()