# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# My plan
# have a pointer pointing to head
# have another pointer to nothing
# iterate the list as long as there is a node
# the next node is saved in a variable
# the link between current and precious nodes is reversed
# the previous pointer points to the current node
# the current pointer points to the next node
# return the previous node

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        previous = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous
