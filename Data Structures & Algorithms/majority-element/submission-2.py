from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #using Boyer-Moore Voting
        #hint - question says always one element is present which is higher
        #in that case the higher frequency element will atleast have one vote
        count = 1
        candidate = nums[0]
        for num in range (1, len(nums)):
            if candidate == nums[num]:
                count += 1
            else:
                count -= 1
            if count <= 0:
                candidate = nums[num]
        return candidate
            

        