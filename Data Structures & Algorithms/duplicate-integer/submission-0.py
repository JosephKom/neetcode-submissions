class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = {}
        for n in nums:
            if n in myMap:
                myMap[n] += 1
            else:
                myMap[n] = 1

        for key in myMap:
            if myMap[key] > 1:
                return True
        return False
        
        
                