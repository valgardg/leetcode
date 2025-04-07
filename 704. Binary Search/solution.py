from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        mp = len(nums) // 2

        while lp != rp:
            # print(f"lp: {lp} - mp: {mp} - rp: {rp}")
            current_val = nums[mp]
            if current_val == target:
                return mp
            if lp == mp or mp == rp:
                if nums[lp] == target:
                    return lp
                if nums[rp] == target:
                    return rp
                return -1
            if current_val > target:
                rp = mp
                mp = (rp + lp) // 2
            elif current_val < target:
                lp = mp
                mp = (rp + lp) // 2

        if nums[lp] == target:
            return lp
        return -1
