from typing import List
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # bad = [k]
        # good = []

        # for inv in invocations:
        #     if k == inv[0]:
        #         bad.append(inv[1])
        #     elif inv[1] in bad:
        #         bad.remove(inv[1])
        #     good.extend(inv)
        # goodset = set(good)
        # goodlist = list(goodset)
        # for b in bad:
        #     if b in goodlist:
        #         goodlist.remove(b)
            
        # return goodlist

        inved = []
        am = [i for i in range(n) if i != k]
        sm = []

        for inv in invocations:
            # gather all methods
            am.extend(inv)
            if k == inv[0]:
                sm.extend(inv)
            inved.append(inv[1])

        for inv in invocations[::-1]:
            if inv[0] in sm:
                sm.append(inv[1])

        sm = list(set(sm))

        # print(f'initial sus methods: {sm}')
        # print(f'invoked methods: {inved}')
        for inv in invocations:
            if inv[0] not in sm and inv[1] in sm:
                sm.remove(inv[1])
            if inv[0] in sm and inv[1] in inved:
                sm.remove(inv[0])

        am = list(set(am))
        sm = list(set(sm))


        for s in sm:
            if s in am:
                am.remove(s)
            
        # print(f'final sus methods: {sm}')
        return am

print(Solution().remainingMethods(4, 1, [[1,2],[0,1],[3,2]]))
print(Solution().remainingMethods(5, 0, [[1,2],[0,2],[0,1],[3,4]]))
print(Solution().remainingMethods(3, 2, [[1,2],[0,1],[2,0]]))
print(Solution().remainingMethods(2, 0, []))
print(Solution().remainingMethods(3, 2, [[1,0], [2,0]]))