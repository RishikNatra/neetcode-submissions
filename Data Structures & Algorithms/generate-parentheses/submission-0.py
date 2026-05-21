class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def rec(l, r):
            if (l == r == n):
                res.append("".join(stack))
                return
            if l < n:
                stack.append("(")
                rec(l+1, r)
                stack.pop()
            if r < l:
                stack.append(")")
                rec(l, r+1)
                stack.pop()

        rec(0,0)
        return res
            
            