class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}

        for i in range(len(strs)):
            x = "".join(sorted(strs[i]))
            if x in myMap:
                myMap[x].append(strs[i])
            else:
                myMap[x] = [(strs[i])]
        return list(myMap.values())