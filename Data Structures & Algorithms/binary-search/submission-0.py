class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            n = l + ((r-l)//2)
            if nums[n] > target:
                r = n-1
            elif nums[n] < target:
                l = n+1
            else:
                return n
        return -1