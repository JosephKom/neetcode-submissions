class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        counts = Counter(nums)

        sorted_list = sorted(nums, key=lambda x: -counts[x])
        frequent = []
        i = 0
        while k > 0:
            if sorted_list[i] not in myMap:
                frequent.append(sorted_list[i])
                myMap.setdefault(sorted_list[i], 1)
                k -= 1
            i += 1
        return frequent 
