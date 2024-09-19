from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])

        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i-k]

            maxSum = max(maxSum, currSum)
        
        print(maxSum/k)
        return maxSum / k

Solution().findMaxAverage([4,0,4,3,3], 5)
Solution().findMaxAverage([0,1,1,3,3], 4)
Solution().findMaxAverage([1,12,-5,-6,50,3], 4)
Solution().findMaxAverage([5], 1)