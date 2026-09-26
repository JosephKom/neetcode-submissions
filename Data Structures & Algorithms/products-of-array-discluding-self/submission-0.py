class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixSum = [0] * len(nums)
        postfixSum = [0] * len(nums)
        prefixSum[0] = nums[0]
        postfixSum[-1] = nums[-1]
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i - 1] * nums[i]
        for j in range(len(nums) - 2, -1, -1):
            postfixSum[j] = postfixSum[j + 1] * nums[j]
        
        result = [0] * len(nums)
        result[0] = postfixSum[1]
        result[-1] = prefixSum[-2]
        
        for k in range(1, len(nums) - 1):
            result[k] = prefixSum[k - 1] * postfixSum[k + 1]
        return result

        
        