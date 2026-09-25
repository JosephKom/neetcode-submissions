class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        newmap = {}
        for i, n in enumerate(numbers, start = 1):
            diff = target - n
            if diff in newmap and newmap[diff] > i:
                return [i,newmap[diff]]
            elif diff in newmap and newmap[diff] < i:
                return [newmap[diff],i]
            newmap[n] = i
        