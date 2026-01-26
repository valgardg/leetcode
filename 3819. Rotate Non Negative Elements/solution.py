class Solution(object):
    def rotateElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        indexes, values = [], []

        for i in range(len(nums)):
            if nums[i] >= 0:
                indexes.append(i)
                values.append(nums[i])

        if len(indexes) == 0 or k == 0:
            return nums

        k = k % len(values)
        # perform elegant af rotation
        values = values[k:] + values[:k]

        for i, val in zip(indexes, values):
            nums[i] = val
        
        return nums

print(Solution().rotateElements([1,-2,3,-4], 3))
# print(Solution().rotateElements([-3,-2,7], 1))
# print(Solution().rotateElements([5,4,-9,6], 2))
print(Solution().rotateElements([0], 4))
# print(Solution().rotateElements([-20,-13,0,24], 76135))
print(Solution().rotateElements([3, 11], 4))
