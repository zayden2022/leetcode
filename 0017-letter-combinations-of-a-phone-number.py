# https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        results = []
        for ch in digits:
            if len(results) == 0:
                results = mapping[ch]
            else:
                left = results
                right = mapping[ch]
                results = []
                for a in left:
                    for b in right:
                        results.append(a+b)
        return results
    
