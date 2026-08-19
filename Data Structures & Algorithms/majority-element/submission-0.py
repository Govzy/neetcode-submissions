from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency_map = defaultdict(int)
        for num in nums:
            frequency_map[num] += 1
        return max(frequency_map, key = frequency_map.get)
        