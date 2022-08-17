#Runtime: 108 ms, faster than 55.74% of Python3 online submissions for Two Sum.
#Memory Usage: 15.1 MB, less than 64.41% of Python3 online submissions for Two Sum.

# -- Solution 1: Brute Force --
# Time: O(n^2)
# Space: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# -- Solution 2: One-pass Hash Table --
# Time: O(n)
# Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in mapping:
                return [i, mapping[compliment]]
            mapping[nums[i]] = i

            