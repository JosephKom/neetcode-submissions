class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s1 = list(s)
        t1 = list(t)
        s1.sort()
        t1.sort()

        if t1 != s1:
            return False
        return True



            

