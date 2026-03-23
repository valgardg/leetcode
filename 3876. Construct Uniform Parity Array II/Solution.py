class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums2even = []
        nums2odd = []
        odds = {i: num for i, num in enumerate(nums1) if num % 2 != 0}
        odds = dict(sorted(odds.items(), key=lambda item: item[1]))
        next_smallest_value = None
        if len(odds) > 1:
            smallest_value = list(odds.items())[0]
            next_smallest_value = list(odds.items())[1]
        elif len(odds) == 1:
            smallest_value = list(odds.items())[0]
        else:
            return True

        # print(smallest_value, next_smallest_value)

        for i, num in enumerate(nums1):
            if num % 2 == 0:
                nums2even.append(num)
                if num - smallest_value[1] >= 1:
                    nums2odd.append(0)
            else:
                nums2odd.append(num)
                if i == smallest_value[0] and next_smallest_value == None:
                    continue
                if num - smallest_value[1] >= 1:
                    nums2even.append(0)

        if len(nums2even) == len(nums1):
            return True
            
        if len(nums2odd) == len(nums1):
            return True

        return False
