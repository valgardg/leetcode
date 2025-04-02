from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        valid = ["{}", "[]", "()"]
        push = ["(","[","{"]
        pop = [")","]","}"]

        if len(s) == 0:
            return True
        if len(s) == 1:
            return False

        if s[0] in pop:
            return False

        stack = []

        for c in s:
            if c in push:
                stack.append(c)
            else:
                if len(stack) > 0 and stack[-1] + c in valid:
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        return True

print(Solution().isValid("([()])[][]("))
print(Solution().isValid("(())"))