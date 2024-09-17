class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1 = len(str1)
        topAnswer = ''
        testChar = ''
        for char in str2:
            testChar += char
            if((str1 == (testChar * (l1 // len(testChar))))):
                topAnswer = testChar
        return topAnswer

    def solve(self):
        print(self.gcdOfStrings("ABABAB", "ABAB"))

solution = Solution()
solution.solve()

# testing