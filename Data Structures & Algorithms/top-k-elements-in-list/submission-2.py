class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        visited = set()
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        sorted_list = sorted(nums, key=lambda x: counts[x], reverse=True)
        k_frequent = []
        i = 0
        while k > 0:
            if sorted_list[i] not in visited:
                k_frequent.append(sorted_list[i])
                visited.add(sorted_list[i])
                k -= 1
            i += 1
        return k_frequent