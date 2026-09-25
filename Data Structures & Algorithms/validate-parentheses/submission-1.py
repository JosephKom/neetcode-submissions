class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {"[":"]", "{":"}", "(":")"}
        for i in range(len(s)):
            if self.openBrace(s[i]):
                stack.append(s[i])
                continue 
            if len(stack) == 0 or match[stack[-1]] != s[i]:
                return False
            stack.pop()
        if len(stack) == 0:
            return True
        return False
            
        
    def openBrace(self, s):
        if (s == "(" or s == "[" or s == "{"):
            return True
        return False