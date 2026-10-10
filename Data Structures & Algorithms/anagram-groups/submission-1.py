class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = defaultdict(list)


        for s in strs:
            res = [0] * 26

            for c in s:
                res[ord(c) - ord("a")] += 1
            
            myMap[tuple(res)].append(s)

        return list(myMap.values())


