class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        sorted_input = sorted(nums)
        for i in range(1,len(sorted_input)):
            if sorted_input[i-1] == sorted_input[i]:
                return True
        return False