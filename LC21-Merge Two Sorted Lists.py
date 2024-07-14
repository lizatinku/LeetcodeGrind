# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# My plan
# have a dummy node as the forst node to start merging right away
# set 2 pointers at the starting of both lists to traverse it
# have a while loop to comapre current nodes of l1 and l2
# Attach the smaller node to the current pointer and move the pointer of the list from which the node was taken.
# compare both list's current nodes again. This continues until both lists are finished
# if list finished but th other doesn't, the rest of unfinished list can be added directly to the merged list 
# return the merged list

# Concepts
# A linked list contains nodes. Each node has a data part and a pointer which points to the next node. The starting node is called head and the ending node is called tail. 
# We use dummy node to avoid an edge case

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
        dummy = ListNode()
        current =  dummy

        l1, l2 = list1, list2 

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            
            current = current.next 


                
        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        return dummy.next 

        
