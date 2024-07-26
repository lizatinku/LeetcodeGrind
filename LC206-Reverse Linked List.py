# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# My plan
# have a pointer pointing to head
# have another pointer to None
# iterate the list as long as there is a node
# save the next node in a variable
# reverse the link between current and previous node
# move the previous pointer to the current node
# move the current pointer to the next node
# return the previous pointer 

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
