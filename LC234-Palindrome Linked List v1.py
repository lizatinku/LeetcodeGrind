# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# My plan
# create an empty stack
# initialize a slow pointer to the head of the list
# initialize a fast pointer to the head of the list
# iterate the linked list as long as fast pointer is not pointing to none
#   move the slow pointer by 1 step
#   move the fast pointer by 2 steps
# If the fast pointer is not None after the loop, it means the linked list has an odd number of elements, so move the slow pointer one step forward to skip the middle element
# iterate the linked list using a while loop as long as slow is not pointing to anything
# pop the element in the stack and assign it to a variable
# For each node, pop the top element from the stack and compare it with the current node’s value.
#   if not, return false
#   if yes, return true

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        stack = []
        slow = head
        fast = head
        
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next
        
        while slow:
            top = stack.pop()
            if slow.val != top:
                return False
            slow = slow.next
        
        return True
