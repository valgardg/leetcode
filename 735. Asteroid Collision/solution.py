from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        final = []

        pp = 0
        print(f'------ {pp} -------')

        while pp != len(asteroids):
            if asteroids[pp] < 0:
                if (len(final) < 1):
                    print(f'appending pointer: {asteroids[pp]}')
                    final.append(asteroids[pp])
                else:
                    pv = final.pop() # previous value
                    print(f'pv popped: {pv}')
                    print(final)
                    if(pv < 0):
                        print(f'appending pv and pointer: {pv} and {asteroids[pp]}')
                        final.append(pv)
                        final.append(asteroids[pp])
                    # collision
                    else:
                        print(f'collision between: {pv} and {asteroids[pp]}')
                        if abs(pv) > abs(asteroids[pp]):
                            print(f'{pv} (pv) appended')
                            final.append(pv)
                        elif abs(pv) == abs(asteroids[pp]):
                            print(f'destroyed')
                            pass
                        else:
                            final.append(asteroids[pp])
                            print(f'{asteroids[pp]} asteroids[pp] appended')

            else:
                print(f'appending pointer: {asteroids[pp]}')
                final.append(asteroids[pp])

            pp += 1
            print(final)
            print(f'------ {pp} -------')
        return final

# print(Solution().asteroidCollision([5,10,-5]))
# print(Solution().asteroidCollision([8, -8]))
# print(Solution().asteroidCollision([10,2,-5]))
# print(Solution().asteroidCollision([-2,-1,1,2]))
# print(Solution().asteroidCollision([-2,1,-2,-1]))
print(Solution().asteroidCollision([10,2,-5]))