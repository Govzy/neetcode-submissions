class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_list = []
        product = 1
        zero_count = 0
        for i in range (0, len(nums)):
            if nums[i] != 0:
                product = product * nums[i]
            else:
                zero_count += 1

        for j in range(0, len(nums)):
            if zero_count == 1:
                if nums[j] != 0:
                    result_list.append(0)    
                else:
                    result_list.append(product)
            elif zero_count > 1:
                result_list.append(0)
            else:
                result_list.append(product // nums[j])        
        return result_list