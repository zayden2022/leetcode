# https://leetcode.com/problems/palindrome-linked-list/
# 
# Algorithm for O(n) time and O(1) space solution:
#   - calc length of the list
#   - reverse first half of the list
#   - compare two sublists
#   - reverse first half again

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = self.calcListLength(head)
        
        if length <= 1:
            return True
        
        result = True
        
        left_half = head
        search = head
        steps = length // 2 - 1
        while steps > 0:
            search = search.next
            steps -= 1
        middle = search.next
        right_half = middle
        if length % 2 == 1:
            right_half = middle.next
        last_left_node = search
        last_left_node.next = None # terminating left_half list
        
        left_half = self.reverseList(left_half)
        
        left_cursor = left_half
        right_cursor = right_half
        steps = length // 2
        while steps > 0:
            if left_cursor.val != right_cursor.val:
                result = False
                break
            left_cursor = left_cursor.next
            right_cursor = right_cursor.next
            steps -= 1
            
        left_half = self.reverseList(left_half)
        last_left_node.next = middle

        return result
            
            
    def calcListLength(self, head: Optional[ListNode]) -> int:
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length
    
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        while head is not None:
            node = head
            head = node.next
            node.next = new_head
            new_head = node
        return new_head
