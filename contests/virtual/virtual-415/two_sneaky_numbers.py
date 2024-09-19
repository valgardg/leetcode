from typing import List
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        found = []
        sneaky = []
        for num in nums:
            if num not in found:
                found.append(num)
            else:
                sneaky.append(num)
        print(sneaky)
        return sneaky                           