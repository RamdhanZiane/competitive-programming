class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        removal = 0
        for l in s[::-1]:
            if removal > 0 and l != '*':
                removal -= 1
            elif l == '*':
                removal += 1
            else:
                ans.append(l)
        return ''.join(ans)[::-1]