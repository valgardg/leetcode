# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import math
from typing import Optional
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cn = head # current node
        cnt = 1 # count
        while cn.next != None:
            cnt += 1
            cn = cn.next

        middleIndex = math.floor(cnt/2)
        print(middleIndex)

        if cnt == 2:
            cn = head
            cn.next = None
            return cn

        cn = head
        cnt = 0
        prev = None
        while cn.next != None:
            if cnt == middleIndex:
                prev.next = cn.next
                return head
            prev = cn
            cnt += 1
            cn = cn.next

print(Solution().findMiddle([1]))
print(Solution().findMiddle([2,2]))
print(Solution().findMiddle([3,3,3]))
print(Solution().findMiddle([4,4,4,4]))
print(Solution().findMiddle([5,5,5,5,5]))