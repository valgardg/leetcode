from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_array = []
        max_array = [float('-inf')] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                min_array.append(nums[i])
            else:
                if min_array[i-1] > nums[i]:
                    min_array.append(nums[i])
                else:
                    min_array.append(min_array[i-1])
        for i in range(len(nums)-1, -1, -1):
            if(i == len(nums)-1):
                max_array[i] = nums[i]
            else:
                if nums[i] > max_array[i+1]:
                    max_array[i] = nums[i]
                else:
                    max_array[i] = max_array[i+1]
        # max_array.reverse()

        # return max_array
    
        for i in range(len(nums)):
            if (min_array[i] < nums[i] < max_array[i]):
                # print(min_array[i], nums[i], max_array[i])
                # print(f'{min_array}\n{nums}\n{max_array}')
                return True
        return False


solution = Solution()
print(solution.increasingTriplet([4,5,2147483647,1,2]))
print(solution.increasingTriplet([5,4,3,2,1]))
print(solution.increasingTriplet([2,1,5,0,4,6]))
print(solution.increasingTriplet([0,4,2,1,0,-1,-3]))