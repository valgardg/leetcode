from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pn = None
        cn = head

        while cn != None:
            nn = cn.next
            cn.next = pn
            pn = cn
            cn = nn

        return pn