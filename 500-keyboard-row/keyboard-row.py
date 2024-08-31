class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1,r2,r3=set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")

        ans=[]
        for word in words:
            if set(word.lower()).issubset(r1) or set(word.lower()).issubset(r2) or set(word.lower()).issubset(r3):
                ans.append(word)
        return ans