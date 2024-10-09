class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op = []
        cp = []
        for p in s:
            if p == '(':
                op.append(p)
            else:
                if len(op) > 0:
                    op.pop()
                else:
                    cp.append(p)
        # print(f'op: {op}, cp: {cp}')
        return len(op) + len(cp)

print(Solution().minAddToMakeValid("()))(("))
print(Solution().minAddToMakeValid("())"))
print(Solution().minAddToMakeValid("((("))