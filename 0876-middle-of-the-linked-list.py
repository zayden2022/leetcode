# https://leetcode.com/problems/middle-of-the-linked-list/
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        steps = self.calcListLength(head) // 2
        while steps > 0:
            head = head.next
            steps -= 1
        return head
    
    def calcListLength(self, head: Optional[ListNode]) -> int:
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length
