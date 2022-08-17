# Runtime: 146 ms, faster than 83.18% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Memory Usage: 15.2 MB, less than 6.68% of Python3 online submissions for Two Sum II - Input Array Is Sorted.

# Time: O(n)
# Space: O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(numbers)):
            compliment = target - numbers[i]
            if compliment in mapping:
                return [mapping[compliment]+1, i+1]
            mapping[numbers[i]] = i