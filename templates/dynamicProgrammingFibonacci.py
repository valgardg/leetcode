class Solution(object):
    mem = {}
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.mem:
            return self.mem[n]
        if n <= 1:
            return n
        self.mem[n] = self.fib(n-1) + self.fib(n-2)
        return self.mem[n]
