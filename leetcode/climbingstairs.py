class Solution:
    def climbStairs(self, n: int) -> int:
        l=[]
        l.append(0)
        l.append(1)
        l.append(2)
        for i in range(3,n+1):
            ll=l[i-1]+l[i-2]
            l.append(ll)
        return l[n]    
            
