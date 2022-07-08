# https://leetcode.com/problems/ransom-note
    
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for l in magazine:
            letters[l] = letters.get(l, 0) + 1
        for l in ransomNote:
            avail = letters.get(l, 0)
            if avail == 0:
                return False
            letters[l] = avail - 1
        return True
