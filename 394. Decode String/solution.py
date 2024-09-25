class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        ss = '' # substring
        nn = '' # number

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                while stack and stack[-1] != '[':
                    ss += (stack.pop())
                stack.pop()
                while stack and stack[-1].isdigit():
                    nn += stack.pop()
                
                print(f'{nn}')
                print(f'multiple: {int(nn[::-1])}, substring: {ss[::-1]}')

                for val in list(int(nn[::-1]) * ss[::-1]):
                    stack.append(val)
                # print(stack)
                ss = ''
                nn = ''

        return ''.join(stack)

# print(Solution().decodeString('3[a]2[bc3[x]]'))
print(Solution().decodeString('100[leetcode]'))