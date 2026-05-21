class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}

        for i, n in enumerate(nums):
            ind[n] = i

        for i, n in enumerate(nums):
            d = target - n
            if d in ind and ind[d] != i:
                return [i, ind[d]]
            