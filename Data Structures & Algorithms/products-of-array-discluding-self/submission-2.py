class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        res = [1] * n
        x = 0
        y = n-1
        product = 1
        for i in range(n):
            product = product*nums[i]
            prefix[i] = product
            x = x + 1
        product = 1
        for i in range(n):
            product = product * nums[y]
            postfix[y] = product
            y = y - 1

        for i in range(n):
            if i == 0:
                res[i] = postfix[i+1]
            elif i == n-1:
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1] * postfix[i+1]

        return res
            