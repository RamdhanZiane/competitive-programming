class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        paren = 0
        stack = []
        0 + 2*1
        '((())())()'
        ans = 0
        cur = None
        for c in s:
            if c == '(':
                print(stack)
                paren += 1
                if cur is not None:
                    stack.append(cur)
                cur = 0
            else:
                print(stack)
                paren -= 1
                val = 0
                if paren > 0:
                    val = stack.pop()
                if cur == 0:
                    cur = 1
                else:
                    cur *= 2
                cur = cur + val
        while stack:
            cur = cur + stack.pop()
        return cur