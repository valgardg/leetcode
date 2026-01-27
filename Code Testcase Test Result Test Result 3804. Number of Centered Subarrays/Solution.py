class Solution(object):
    def centeredSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i, num in zip(range(len(nums)), nums):

            checklist = [num]

            for ii, second_num in zip(range(len(nums)), nums[i+1:]):

                checklist.append(second_num)
                listsum = sum(checklist)
                if(listsum in checklist):
                    count += 1

        return count + len(nums)

print(Solution().centeredSubarrays([0,-1,1]))
print(Solution().centeredSubarrays([2,3]))
