'''2. Add Two Numbers
Medium
Topics
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        output = []
        n1 = self.getNumberFromList(l1)
        n2 = self.getNumberFromList(l2)
        print(n1)
        print(n2)
        print(n1 + n2)
        return output
    
    def getNumberFromList(self, theList):
        # theList = theList[::-1]
        theNumber = 0
        for index in range(len(theList)):
            exp = 10**(index)
            theNumber += theList[index] * exp
        return theNumber
    
def main():
    sol = Solution().addTwoNumbers([2,4,3],[5,6,4])
    # expected: 
    # [2,42,38,0,43,21,5,7,12,12,13,23,24,24,27,29,30,31,33,48]
    
    print(sol)

if __name__ == "__main__":
    main()