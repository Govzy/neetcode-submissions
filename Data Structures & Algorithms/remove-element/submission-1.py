class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == val and nums[j]!= val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[i] == val and nums[j] == val:
                j += 1
            else:
                i += 1
                j += 1
        count = 0
        for n in nums:
            if n != val:
                count += 1
        return count


            