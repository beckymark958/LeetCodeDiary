# -- Solution 1: Hashset --

# Time: O(M+N)
# Space: O(M) or O(N)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        current_a = headA
        current_b = headB
        hashset = set()
        
        while current_a:
            hashset.add(current_a)
            current_a = current_a.next
        
        while current_b:
            if current_b in hashset:
                return current_b
            current_b = current_b.next
        return None


# -- Solution 2: Two Pointers --

# Time: O(M+N)
# Space: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        current_a = headA
        current_b = headB
        
        while current_a != current_b:
            current_a = current_a.next if current_a else headB
            current_b = current_b.next if current_b else headA
            
        return current_a
