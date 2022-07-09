# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        for customer in accounts:
            wealth = sum(customer)
            if wealth > result:
                result = wealth
        return result
