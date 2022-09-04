# Time: O(n)
# Space: O(n)

# -- Solution: Monotonic Stack --
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        nextSmallerIdx = self.nextSmaller(arr)
        prevSmallerIdx = self.prevSmaller(arr)
        
        total = 0
        M=1e9 + 7
        for i in range(len(arr)):
            upper = nextSmallerIdx[i]
            lower = prevSmallerIdx[i]
            
            num = (upper - i) * (i - lower) * arr[i] %M
            total += num %M
        
        return int(total %M)
        
    def nextSmaller(self, arr):
        nextSmallerIdx =  [len(arr)] * len(arr)  # [next_smaller_idx]
        stack = [] #index

        for i in range(len(arr)):
            while (len(stack)!= 0) and (arr[i] < arr[stack[-1]]):
                nextSmallerIdx[stack[-1]] = i
                stack.pop()
            stack.append(i)
        return nextSmallerIdx


    def prevSmaller(self, arr):
        prevSmallerIdx = [-1] * len(arr)  # [prev_smaller_idx]
        stack = [] #index

        for i in range(len(arr)-1, -1, -1):
            while (len(stack)!= 0) and (arr[i] <= arr[stack[-1]]):
                prevSmallerIdx[stack[-1]] = i
                stack.pop()
            stack.append(i)
        return prevSmallerIdx