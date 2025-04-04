from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers)-1
        s = numbers[lp] + numbers[rp]
        while s != target:
            if s > target:
                rp -= 1
            elif s < target:
                lp += 1
            s = numbers[lp] + numbers[rp]
            
        return [lp+1,rp+1]
        
    
print(Solution().twoSum([2,7,11,14], 9))
print(Solution().twoSum([5,25,75], 100))
print(Solution().twoSum([3,24,50,79,88,150,345], 200))
print(Solution().twoSum([1,2,3,4,4,9,56,90], 8))
print(Solution().twoSum([12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997], 542))

# HASH MAP SOLUTION BELOW (NOT OPTIMAL AS QUESTION STATES: "Your solution must use only constant extra space", WHERE HASH MAP USES O(n))
# from typing import List
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         hm = {}
#         for i in range(len(numbers)):
#             num = numbers[i]
#             diff = target - num
#             if diff in hm:
#                 # print(f'{diff} and {num} add up to {target}')
#                 # print(f'return indexes {i} and {hm[diff]}')
#                 return [hm[diff] + 1, i + 1]
#             else:
#                 hm[num] = i

#         return "you done messed tf up"

# print(Solution().twoSum([2,7,11,15], 9))
# print(Solution().twoSum([2,3,4], 6))
# print(Solution().twoSum([-1,0], -1))