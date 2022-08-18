# Runtime: 129 ms, faster than 32.15% of Python3 online submissions for High Five.
# Memory Usage: 14.2 MB, less than 44.57% of Python3 online submissions for High Five.

# Time: O(n)
# Space: O(n)
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        ans = []
        hash_map = {}
        for item in items:
            id = item[0]
            score = item[1]
            if id not in hash_map:
                hash_map[id] = [score]
            else:
                hash_map[id].append(score)
        
        sorted_keys = sorted(hash_map.keys())
        for id in sorted_keys:
            avg = int(sum(sorted(hash_map[id], reverse = True)[:5])/5)
            ans.append([id, avg])
        return ans