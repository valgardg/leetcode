class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        new_int = 0
        strn = str(bin(n))[2:]
        for i, num in enumerate(("0" * (32 - len(strn))) + strn):
            num = int(num)
            if i == 0:
                new_int += num
            else:
                new_int += num * 2**i

        return new_int
    

print(Solution().reverseBits(43261596))
