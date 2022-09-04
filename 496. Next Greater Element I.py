# Time: O(n)
# Space: O(n)

# -- Solution: Monotonic Stack --
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        mapping = {}  # {val, next_greater_val}
        stack = []  # index
        
        for i in range(len(nums2)):
            while (len(stack)!= 0) and (nums2[i] > nums2[stack[-1]]):
                mapping[nums2[stack[-1]]] = nums2[i]
                stack.pop()
            stack.append(i)
            
        for x in nums1:
            if x in mapping:
                ans.append(mapping[x])
            else:
                ans.append(-1)
            
        return ans