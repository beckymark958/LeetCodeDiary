# -- Solution 1: Sorting --

# Time: O(n logn)
# Space: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_sort = sorted(s)
        t_sort = sorted(t)
        
        if s_sort == t_sort:
            return True
        return False


# -- Solution 2: Frequency Counter Table --

# Time: O(n)
# Space: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letter_count = {}
        
        for i in s:
            if i not in letter_count:
                letter_count[i] = 1
            else:
                letter_count[i] += 1
        
        for j in t:
            if j not in letter_count:
                return False
            else:
                letter_count[j] -= 1
        
        for val in letter_count.values():
            if val != 0:
                return False
        
        return True
