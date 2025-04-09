from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []

        for i in range(len(nums)):
            num = nums[i]
            twoSumHM = {}
            target = 0 - num
            print(f"Num: {num} - Targret: {target}")
            for j in range(len(nums)):
                if j == i:
                    continue
                tnum = nums[j]
                other = target - tnum
                # check if we have the other number
                if other in twoSumHM.keys():
                    for other_index in twoSumHM[other]:
                        entry = [nums[i],nums[j],nums[other_index]]
                        # entry = [i,j,other_index] 
                        if sorted(entry) not in solutions: 
                            solutions.append(sorted(entry))
                    
                # add current num and index
                if tnum in twoSumHM.keys():
                    twoSumHM[tnum].append(j)
                else:
                    twoSumHM[tnum] = [j]

        return solutions
                

print(Solution().threeSum([-1,0,1,2,-1,-4]))