class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        sortednums = sorted([int(num, 2) for num in nums])
        for i in range(max(2**len(nums[0]) - 1, 2)):
            if i not in sortednums:
                return bin(i)[2:].zfill(len(nums[0]))
