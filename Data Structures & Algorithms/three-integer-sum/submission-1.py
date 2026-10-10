class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        myMap = defaultdict(list)
        nums.sort()

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                vals = list()
                target = -nums[i]
                total = nums[l] + nums[r]
                if target == total:
                    vals.append(nums[i])
                    vals.append(nums[l])
                    vals.append(nums[r])
                    if tuple(vals) not in myMap and len(vals) == 3:
                        myMap[tuple(vals)].append(1)
                    l += 1
                elif total < target:
                    l += 1
                elif total > target:
                    r -= 1
        return list(myMap.keys())


            