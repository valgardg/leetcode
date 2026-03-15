class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        if n < 1000:
            return 0
        # thousands
        for i in range(4, len(str(n))+1, 3):
            # minus value
            min_val = int("1" + ("0" * (i - 1)))
            total_commas += n - min_val + 1
        return total_commas
