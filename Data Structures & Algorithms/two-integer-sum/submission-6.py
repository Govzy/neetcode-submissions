class Solution:
    # Time Complexity: O(n log n)
    #   - Building index_value_pairs with enumerate takes O(n)
    #   - Sorting index_value_pairs takes O(n log n)  <- this dominates
    #   - The two-pointer while loop takes O(n)
    #   Overall: O(n) + O(n log n) + O(n) = O(n log n)
    #
    # Space Complexity: O(n)
    #   - index_value_pairs stores n (index, value) pairs, so O(n) extra space
    def twoSum(self, bums: List[int], target: int) -> List[int]:
        # Step 1: Pair each value with its original index
        # e.g. bums = [30, 10, 20] -> [(0, 30), (1, 10), (2, 20)]
        index_value_pairs = list(enumerate(bums))

        # Step 2: Sort those pairs by value (position 1 in each pair)
        index_value_pairs.sort(key=lambda pair: pair[1])

        # Step 3: Two-pointer search on the sorted pairs
        left = 0
        right = len(index_value_pairs) - 1

        while left < right:
            left_index, left_value = index_value_pairs[left]
            right_index, right_value = index_value_pairs[right]

            current_sum = left_value + right_value

            if current_sum == target:
                # left_index and right_index are original positions,
                # but after sorting, the LARGER original index can end up
                # on the "left" pointer (e.g. nums=[-1,-2,-3,-4,-5], target=-8
                # gives left_index=4, right_index=2). Sort them so the
                # smaller index always comes first, matching expected output.
                return sorted([left_index, right_index])
            elif current_sum > target:
                right -= 1
            else:
                left += 1

        return []