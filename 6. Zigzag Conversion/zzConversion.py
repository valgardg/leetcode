class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        largeList = [[] for i in range(numRows)]
        print(largeList)
        print(list(s))
        print(list(s)[0::4])
        print(list(s)[1::4])

def main():
    sol = Solution().convert("PAYPALISHIRING", 3)
    # expected: "PAHNAPLSIIGYIR"
    print(sol)

if __name__ == "__main__":
    main()