from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0

        rows = {}
        cols = {}

        n = len(grid)
        ngrid = [] # new grid

        for row in grid:
            for col in row:
                ngrid.append(col)

        print(f'ngrid: {ngrid}')

        for i in range(n):
            row = ngrid[i*n:(i*n)+n]
            # print(row)
            if str(row) in rows:
                rows[str(row)] += 1
            else:
                rows[str(row)] = 1

        print('---------')

        for i in range(n):
            col = ngrid[i::n]
            # print(col)
            if str(col) in rows:
                count += 1 * rows[str(col)]

        return count    


print(Solution().equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))