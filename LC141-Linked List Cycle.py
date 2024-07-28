# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# My plan
# If the head of the list is none, return false immediately, as an empty list cannot have a cycle.
# initialize a slow pointer pointing at the head of the list
# initialize a fast pointer to head.next instead of head to avoid the initial false positive when slow and fast are both pointing at the same node.
# have a while loop to traverse the list that continues as long as fast and fast.next are not none
# if the fast meet the slow, return true because there is a cycle
# Move the fast pointer by 2 steps and the slow pointer by 1 step
# Else, return false

# Concepts learnt:
# 1. Floyd's Tortise and Hare or Slow and Fast: This algorithm uses two pointers that move at different speeds to detect cycles in a sequence. It is commonly used in linked list problems to detect cycles efficiently.
# 2. Linked lists: is a data structure consisting of nodes, where each node contains a value and a pointer to the next node in the sequence. They are dynamic in size, allowing efficient insertions and deletions, but they have slower access times compared to arrays due to their sequential nature.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return None

        slow, fast = head, head.next

        while fast and fast.next:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next

        return False
