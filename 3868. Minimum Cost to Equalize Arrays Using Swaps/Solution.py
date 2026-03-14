from collections import defaultdict
class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        total_cost = 0 

        num_counts = defaultdict(int)
        nums1_counts = defaultdict(int)
        nums2_counts = defaultdict(int)
        
        for num in nums1:
            num_counts[num] += 1
            nums1_counts[num] += 1
        for num in nums2:
            num_counts[num] += 1
            nums2_counts[num] += 1

        if nums1_counts == nums2_counts:
            return 0

        for num, count in num_counts.items():
            if count % 2 != 0:
                return -1

        for num, count in nums1_counts.items():
            extras = count - (num_counts[num] - count)
            if extras > 0:
                total_cost += extras // 2


        return total_cost 




# print(Solution().minCost([1,1], [1,2]))
# print(Solution().minCost([10,10], [20, 20]))
# print(Solution().minCost([10,20], [20, 10]))
# print(Solution().minCost([1,1,1], [1,2,2]))
# print(Solution().minCost([1,1,2], [1,2,2]))
# print(Solution().minCost([1,1,2], [2,2,2]))
# print(Solution().minCost([10,20], [30,40]))
