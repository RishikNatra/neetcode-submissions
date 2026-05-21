from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        arr = []

        for word in strs:
            sorted_s = tuple(sorted(word))
            sol[sorted_s].append(word)

        for res in sol.values():
            arr.append(res)
        return arr
