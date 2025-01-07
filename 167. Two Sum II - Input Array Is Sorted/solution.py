from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(numbers)):
            num = numbers[i]
            diff = target - num
            if diff in hm:
                # print(f'{diff} and {num} add up to {target}')
                # print(f'return indexes {i} and {hm[diff]}')
                return [hm[diff] + 1, i + 1]
            else:
                hm[num] = i

        return "you done messed tf up"

print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([2,3,4], 6))
print(Solution().twoSum([-1,0], -1))