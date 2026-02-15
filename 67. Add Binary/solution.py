class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum1 = 0
        for i, val in enumerate(a[::-1]):
            val = int(val)
            if i == 0:
                print(f"sum1 + {val * 1}")
                sum1 += val * 1
            else:
                print(f"sum1 + {val * (2 ** i)}")
                sum1 += val * (2 ** i)
        
        print(f"sum1: {sum1}")
        
        sum2 = 0
        for i, val in enumerate(b[::-1]):
            val = int(val)
            if i == 0:
                print(f"sum1 + {val * 1}")
                sum1 += val * 1
            else:
                print(f"sum1 + {val * (2 ** i)}")
                sum1 += val * (2 ** i)
        
        print(sum1, sum2)

        total_sum = sum1 + sum2
        return str(bin(total_sum))[2:]

# print(Solution().addBinary("11", "1"))
print(Solution().addBinary("1010", "1011"))