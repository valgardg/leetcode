class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        binstring = str(bin(n))[2:]
        final = ""
        for c in binstring:
            final += "1" if c == "0" else "0"
        return int(final, 2)
