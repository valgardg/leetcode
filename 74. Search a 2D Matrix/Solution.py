class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        master_list = []
        for row in matrix:
            master_list.extend(row)

        l, r = 0, len(master_list)

        while l < r:
            mid = l + (r - l) // 2
            # print(f"mid: {mid}")
            if(master_list[mid] == target): return True
            if (master_list[mid] > target):
                r = mid
            else:
                l = mid + 1
        return False
