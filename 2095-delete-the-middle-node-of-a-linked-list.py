# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.calcListLength(head)
        if length <= 1:
            return None
        steps = length // 2 - 1
        prev = head
        while steps > 0:
            prev = prev.next
            steps -= 1
        prev.next = prev.next.next
        return head
    
    def calcListLength(self, head: Optional[ListNode]) -> int:
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length        
