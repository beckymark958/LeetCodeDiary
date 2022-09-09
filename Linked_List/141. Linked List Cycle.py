# -- Solution 1: Hashset --

# Time: O(n)
# Space: O(n)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashSet = set()
        
        current = head
        while current!= None:
            if current in hashSet:
                return True
            else:
                hashSet.add(current)
                current = current.next
        return False

# -- Solution 2: Fast & Slow Pointers --

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashSet = set()
        
        current = head
        while current!= None:
            if current in hashSet:
                return True
            else:
                hashSet.add(current)
                current = current.next
        return False
