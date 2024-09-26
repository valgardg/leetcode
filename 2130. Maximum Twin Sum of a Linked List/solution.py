from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        mts = 0 # max twin sum
        n = 1
        cn = head # count node
        while cn.next != None:
            n += 1
            cn = cn.next
        
        print(f'length of list(n): {n}')

        twins = {}
        cnt = 0
        while head != None:
            twin = n - 1 - cnt
            # print(f'twin of node {cnt} is {twin}')

            if twin in twins:
                twinSum = head.val + twins[twin]
                if twinSum > mts:
                    mts = twinSum
            else:
                twins[cnt] = head.val

            cnt += 1
            head = head.next

        # print(twins)

        return mts

head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
answer = (Solution().pairSum(head))
print(answer)