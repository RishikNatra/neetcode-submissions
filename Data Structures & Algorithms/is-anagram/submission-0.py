class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sa= {}
        ta= {}
        for i in range(len(s)):
            sa[s[i]] = 1 + sa.get(s[i], 0)
            ta[t[i]] = 1 + ta.get(t[i], 0)

        for c in sa:
            if sa[c] != ta.get(c, 0):
                return False
        return True

        
