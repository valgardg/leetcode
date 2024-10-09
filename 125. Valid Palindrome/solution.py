class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''
        for char in s:
            if str.isalpha(char):
                ss += (char.lower())
            if char.isnumeric():
                ss += char
        # print(ss)
        return ss == ss[::-1]

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(" "))
print(Solution().isPalindrome("Marge, let's \"[went].\" I await {news} telegram."))
print(Solution().isPalindrome("0P"))
print(Solution().isPalindrome("1a2"))