# -- Solution 1 : One Pointer, Two Passes --

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        current = head
        while current != None:
            current = current.next
            length += 1
        
        if n == length:
            return head.next


        count = 0
        current = head

        while current != None:
            if count != length - n - 1:
                current = current.next
            else:
                current.next = current.next.next
            
            count += 1
        
        return head


# -- Solution 2 : Two Pointers, One Pass --

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:      
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            fast = head
            for i in range(n):
                if fast.next != None:
                    fast = fast.next
                else:
                    return head.next
            
            slow = head
            while fast.next != None:
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next
            return head