from typing import List
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        operations = 0
        previous = grid[0]
        for row in grid[1:]:
            # print(f'row: {row}')
            for i in range(len(row)):
                if row[i] <= previous[i]:
                    required = previous[i] - row[i] + 1
                    # print(f'required: {required}')
                    previous[i] = row[i] + required
                    operations += required
                else:
                    previous[i] = row[i]
        
        return operations
    
print(Solution().minimumOperations([[3,2],[1,3],[3,4],[0,1]]))
print(Solution().minimumOperations([[3,2,1],[2,1,0],[1,2,3]]))