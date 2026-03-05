class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        initial = list(range(n))
        current = list(range(n))
        def apply_operation(n, og_n):
            arr = list(range(og_n))
            for i in range(og_n):
                if i % 2 == 0:
                    arr[i] = n[i / 2]
                else:
                    arr[i] = n[og_n / 2 + (i - 1) / 2]
            return arr
            

        current = apply_operation(current, n)
        count = 1
        while initial != current:
            current = apply_operation(current, n)
            count += 1
                
        return count
