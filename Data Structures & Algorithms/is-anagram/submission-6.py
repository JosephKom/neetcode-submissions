class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        myMap1 = {}
        myMap2 = {}
        for i in range(len(s)):
            if s[i] not in myMap1:
                myMap1.setdefault(s[i], 1)
            else:
                myMap1[s[i]] += 1
            if t[i] not in myMap2:
                myMap2.setdefault(t[i], 1)
            else:
                myMap2[t[i]] += 1
        
        for char in s:
            if char not in myMap2 or myMap1[char] != myMap2[char]:
                return False
        return True
            

