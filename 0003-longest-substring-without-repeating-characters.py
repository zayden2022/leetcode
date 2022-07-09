# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        longest = 1
        for start in range(length-1):
            chars = {}
            index = start
            while True:
                ch = s[index]
                if ch in chars:
                    # found repeated character
                    substr_len = index - start
                    if substr_len > longest:
                        longest = substr_len
                    break
                if index == length - 1:
                    # last char in the string
                    substr_len = index - start + 1
                    if substr_len > longest:
                        longest = substr_len
                    break
                index += 1
                chars[ch] = True
        return longest
