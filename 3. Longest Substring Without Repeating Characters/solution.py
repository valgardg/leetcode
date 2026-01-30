class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        longest = 1
        l,r = 0,0

        string_window = s[0]

        while l < len(s):
            # print(f"string_window: {string_window}")
            # print(f"l,r={l},{r}")
            # base substring length check
            if len(set(string_window)) == len(string_window):
                if (r - l) + 1 > longest:
                    # print(f"Longest unique substring: {string_window}")
                    longest = (r - l) + 1

            if l == r and r < len(s) - 1:
                r += 1
                string_window += s[r]
            else:
                if len(set(string_window)) == len(string_window) and r < len(s) - 1:
                    r += 1
                    string_window += s[r]
                else:
                    l += 1
                    string_window = string_window[1:]

        return longest


print(Solution().lengthOfLongestSubstring("au"))

print(Solution().lengthOfLongestSubstring(""))
print(Solution().lengthOfLongestSubstring(" "))
print(Solution().lengthOfLongestSubstring("c"))
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("valgardisthebest"))
