from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
        nd = {}
        for i in range(len(nums)):
            num = nums[i]
            if (target - num) in nd:
                return [i, nd[target-num]]
            else:
                nd[num] = i
                
print(twoSum([3,2,4], 6))