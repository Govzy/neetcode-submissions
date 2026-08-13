class Solution:
    #Time Complexity sorting 
    def twoSum(self, bums: List[int], target: int) -> List[int]:
        # this method uses sorting
        nums = sorted(bums)
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i]+nums[j] == target:
                match = []
                for k in range(len(bums)):
                    if nums[i] == bums[k] or nums[j] == bums[k]:
                        match.append(k)
                return match
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return []

        