class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        max_len = 0
        for num in nums:
            curr_len = 0
            if (num - 1) not in myset:
                while (num + curr_len) in myset:
                    curr_len += 1
            max_len = max(curr_len, max_len)
        return max_len
    

    
        

                

        
        

            
            

        

