# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        specials = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        res = 0
        length = len(s)
        i = 0
        while i < length:
            last = i == (length - 1)
            if not last:
                sp = s[i:i+2]
                if sp in specials:
                    res += specials[sp]
                    i += 2
                    continue
                    
            res += m[s[i]]
            i += 1
        return res
