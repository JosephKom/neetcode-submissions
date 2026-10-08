class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        longest = 0
        for num in nums:
            curr_len = 0
            if (num - 1) not in myset:
                while (num + curr_len) in myset:
                    curr_len += 1
            longest = max(curr_len, longest)
        return longest
                    

    
        

                

        
        

            
            

        

