class Solution:
    def mySqrt(self, x: int) -> int:
        lastknown = 0
        for i in range(x+1):
            if i * i > x:
                return lastknown
            else:
                lastknown = i
        return lastknown
    
print(Solution().mySqrt(1))