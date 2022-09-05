# -- Solution: --

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        current = dummy.next
        
        while (current != None) and (current.next != None):
            if current.val == current.next.val:
                while (current.next != None) and (current.val == current.next.val):
                    current = current.next
                prev.next = current.next
                current = current.next 
            
            else:
                prev = current
                current = current.next 
        
        return dummy.next