class Solution:
    def reverseWords(self, s: str) -> str:
        word=''
        words=[]
        i=0
        while i<len(s):
            while i<len(s) and s[i]==' ':
                i+=1
            while i<len(s) and s[i]!=' ':
                word+=s[i]
                i+=1
            words.append(word)
            word=''
        print(words)
        return ' '.join(words[::-1]).strip()