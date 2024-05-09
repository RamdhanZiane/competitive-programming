class Solution:
    def decodeString(self, s: str) -> str:
        # ans = []
        # number = []
        # nb_stacks = 0
        # for i in range(len(s)):
        #     if s[i] in map(str,range(10)):
        #         if nb_stacks == 0:
        #             continue
        #         number.append(s[i])
        #     elif s[i] == '[':
        #         nb_stacks += 1
        #         sub = self.decodeString(s[i+1:])
        #         if number == []:
        #             number = ['1']
        #         for _ in range(int(''.join(number))):
        #             ans.append(sub)
        #     elif s[i] == ']':
        #         if nb_stacks == 0:
        #             return ''.join(ans)
        #         nb_stacks -= 1
        #     else:
        #         if nb_stacks == 0:
        #             continue
        #         ans.append(s[i])
        # return ''.join(ans)


        def solve(s, i):
            num = []
            ans = []
            nums = ['0','1','2','3','4','5','6','7','8','9']
            while i < len(s):
                if s[i] in nums:
                    num.append(s[i])
                elif s[i] == '[':
                    i, sub_s = solve(s, i+1)
                    for _ in range(int(''.join(num))):
                        ans.append(sub_s)
                    num = []
                    i = i+1
                    continue
                elif s[i] == ']':
                    return i, ''.join(ans)
                else:
                    ans.append(s[i])
                i+=1
            return i, ans
        a, ans = solve(s,0)
        return ''.join(ans)
