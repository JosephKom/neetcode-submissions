class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] += 1
            else:
                hash.setdefault(nums[i],1)
        
        for j in range(len(nums)):
            if hash.get(nums[j]) > 1:
                return True
        return False


