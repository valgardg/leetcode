from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        pp = 0

        while pp != n:
            if asteroids[pp] < 0:
                if pp == 0:
                    pp += 1
                    pass
                else:
                    pv = asteroids[pp-1]
                    if(pv < 0):
                        pp += 1
                    # collision
                    else:
                        if abs(pv) > abs(asteroids[pp]):
                            asteroids = asteroids[:pp] + asteroids[pp+1:]
                            n -= 1
                            pp -= 1
                        elif abs(pv) == abs(asteroids[pp]):
                            asteroids = asteroids[:pp-1] + asteroids[pp+1:]
                            n -= 2
                            pp -= 2
                        else:
                            asteroids = asteroids[:pp-1] + asteroids[pp:]
                            n -= 1
                            pp -= 1
            else:
                pp += 1
            
            if pp < 0:
                pp = 0
            
        return asteroids

print(Solution().asteroidCollision([5,10,-5]))
print(Solution().asteroidCollision([8, -8]))
print(Solution().asteroidCollision([10,2,-5]))
print(Solution().asteroidCollision([-2,-1,1,2]))
print(Solution().asteroidCollision([-2,1,-2,-1]))
print(Solution().asteroidCollision([10,2,-5]))