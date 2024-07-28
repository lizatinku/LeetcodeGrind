# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# My plan
# have 2 pointers: slow and fast at the start of the linked list
# iterate the linked list as long as the fast pointer doesn't reach the end of the list
# increment the slow pointer by 1
# increment the fast pointer by 2
# return the slow pointer

# Concepts learnt:
# 1. Floyd's Tortise and Hare or Slow and Fast: This algorithm uses two pointers that move at different speeds to detect cycles in a sequence. It is commonly used in linked list problems to detect cycles efficiently.

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
