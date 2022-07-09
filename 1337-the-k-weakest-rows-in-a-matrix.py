# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        power = []
        for i in range(len(mat)):
            power.append(sum(mat[i]))
        results = []
        for x in range(k):
            lowest_index = None
            for i in range(len(power)):
                if power[i] is None:
                    continue
                if lowest_index is None:
                    lowest_index = i
                    continue
                if power[lowest_index] > power[i]:
                    lowest_index = i
            results.append(lowest_index)
            power[lowest_index] = None
        return results
