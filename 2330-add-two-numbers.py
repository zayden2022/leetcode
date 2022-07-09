# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result_head = None
        last = None
        while l1 is not None or l2 is not None:
            a = 0 if l1 is None else l1.val
            b = 0 if l2 is None else l2.val
            val = a + b + carry
            carry = val // 10
            val = val % 10
            if result_head is None:
                result_head = ListNode(val)
                last = result_head
            else:
                last.next = ListNode(val)
                last = last.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry != 0:
            last.next = ListNode(carry)
        return result_head
