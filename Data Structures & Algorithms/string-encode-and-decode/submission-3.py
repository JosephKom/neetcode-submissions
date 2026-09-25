class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for i in range(len(strs)):
            word += strs[i]
            word += "ʨ"
        return word



    def decode(self, s: str) -> List[str]:
        words = []
        word = ""
        for i in range(len(s)):
            if s[i] != "ʨ":
                word += s[i]
            else:
                words.append(word)
                word = ""
        return words
       
