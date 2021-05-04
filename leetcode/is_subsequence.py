class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind=-1
        for i in s:
            t=t[ind+1:]
            if i in t:
                ind=t.index(i)
            else:
                return False
        return True
