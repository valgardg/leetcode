from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums = set(nums)
        for num in nums:
            tslist = [x for x in nums if x != num]
            target = -1 * num
            # 2 sum implementation
            nd = {}
            for nmbr in tslist:
                if target - nmbr in nd:
                    print(f"target: {target}, num: {num}, nmbr: {nmbr}, nd[target - nmbr]: {nd[target - nmbr]}")
                    solutions.append([num, nmbr, nd[target - nmbr]])
                else:
                    nd[nmbr] = nmbr
        return solutions

print(Solution().threeSum([-1,0,1,2,-1,-4]))