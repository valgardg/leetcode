from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a < 0:
                if len(stack) < 1:
                    stack.append(a)
                else:
                    # handle negative asteroid
                    if stack[-1] < 0:
                        stack.append(a)
                    else:
                        pv = stack.pop()
                        if abs(pv) > abs(a):
                            stack.append(pv)
                        elif abs(a) > abs(pv):
                            stack.append(a)
                        
                        while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:
                            v1 = stack.pop()
                            v2 = stack.pop()

                            if abs(v1) > abs(v2):
                                stack.append(v1)
                            elif abs(v2) > abs(v1):
                                stack.append(v2)
            else:
                stack.append(a)
        return stack

print(Solution().asteroidCollision([5,10,-5]))
print(Solution().asteroidCollision([8, -8]))
print(Solution().asteroidCollision([10,2,-5]))
print(Solution().asteroidCollision([-2,-1,1,2]))
print(Solution().asteroidCollision([-2,1,-2,-1]))
print(Solution().asteroidCollision([10,2,-5]))