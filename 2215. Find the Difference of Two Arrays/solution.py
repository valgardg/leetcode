from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        distinct1 = []
        distinct2 = []

        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in distinct1:
                distinct1.append(nums1[i])
            
        for i in range(len(nums2)):
            if nums2[i] not in nums1 and nums2[i] not in distinct2:
                distinct2.append(nums2[i])

        answer = [distinct1, distinct2]

        return answer

print(Solution().findDifference([1,2,3,3], [1,2,2,2]))