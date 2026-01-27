class Solution(object):
    def centeredSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i, num in zip(range(len(nums)), nums):

            checklist = [num]
            running_sum = num

            for ii, second_num in zip(range(len(nums)), nums[i+1:]):

                checklist.append(second_num)
                running_sum = running_sum + second_num
                if(running_sum in checklist):
                    count += 1

        return count + len(nums)

print(Solution().centeredSubarrays([0,-1,1]))
print(Solution().centeredSubarrays([2,3]))
