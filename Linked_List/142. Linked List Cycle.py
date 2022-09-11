# -- Solution 1: Hashset --

# Time: O(n)
# Space: O(n)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashset = set()
        
        current = head
        
        while current:
            if current in hashset:
                return current
            
            hashset.add(current)
            current = current.next
        return None

# -- Solution 2: Fast & Slow Pointers --

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check = fast = slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                while slow != check:
                    check = check.next
                    slow = slow.next
                return check        
        
        return None