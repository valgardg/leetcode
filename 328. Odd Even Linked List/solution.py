from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previousOdd = None
        previousEven = None
        firstEven = None

        cnt = 1

        if head == None or head.next == None:
            return head

        cn = head
        while cn != None:
            # print(f'looking at value {cn.val}')
            if (cnt % 2) == 0:
                if firstEven == None:
                    firstEven = cn
                    # print(f'Making firstEven {cn.val}')
                if previousEven == None:
                    previousEven = cn
                    # print(f'Making previousEven = {cn.val}')
                else:
                    previousEven.next = cn
                    previousEven = cn
                    # print(f'Making previousEven.next = {cn.val} and previousEven = {cn.val}')
            else:
                if previousOdd == None:
                    previousOdd = cn
                    # print(f'Making previousOdd = {cn.val}')
                else:
                    previousOdd.next = cn
                    previousOdd = cn
                    # print(f'Making previousOdd.next = {cn.val} and previousOdd = {cn.val}')
            if(cn.next):
                cn = cn.next
            else:
                break
            cnt += 1

        previousOdd.next = firstEven
        previousEven.next = None

        return head
    
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
answer = (Solution().oddEvenList(head))

print('Answer: ')
x = 0
while answer != None and x < 10:
    print(answer.val)
    answer = answer.next
    x += 1