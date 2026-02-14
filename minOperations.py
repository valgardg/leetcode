class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        binpals = []
        ans = []
        for i in range(1, 5000):
            binary = (str(bin(i)))
            # print(f"{binary[2:]}: {binary[2:]== binary[2:][::-1]}")
            if binary[2:]== binary[2:][::-1]:
                binpals.append(i)

        for i, num in enumerate(nums):
            j = 0
            if num in binpals:
                ans.append(0)
                continue
            while num > binpals[j] and j < len(binpals) - 1:
                j += 1
            ans.append(min(abs(binpals[j] - num), abs(num - binpals[j-1])))


        return ans



print(Solution().minOperations([1,2,4]))
print(Solution().minOperations([6,7,12]))