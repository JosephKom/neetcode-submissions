class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set()
        longest = 0

        for num in nums:
            numbers.add(num)

        for i in range(len(nums)):
            if nums[i] - 1 not in numbers:
                curr_count = 0
                j = 0
                while (nums[i] + j) in numbers:
                    curr_count += 1
                    j += 1
                longest = max(longest, curr_count)
        return longest
                    
            