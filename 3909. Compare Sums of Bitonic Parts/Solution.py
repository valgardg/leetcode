class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        maxval = 0
        maxindex = 0
        ssum = []
        rsum = 0

        nlen = len(nums)

        bsum = []
        brsum = 0

        for i, num in enumerate(nums):
            rsum += num
            ssum.append(rsum)
            if num > maxval:
                maxval = num
                maxindex = i

            brsum += nums[nlen - 1 - i]
            bsum.append(brsum)
        
        sum1 = ssum[maxindex]
        sum2index = (nlen) - 1 - maxindex
        sum2 = bsum[sum2index]

        # print(f"maxindex: {maxindex}")
        # print(f"sum1: {sum1}\nsum2: {sum2}\nssum: {ssum}\nbsum: {bsum}")

        if sum1 > sum2:
            return 0
        if sum2 > sum1:
            return 1
        if sum1 == sum2:
            return -1
        return "what"
