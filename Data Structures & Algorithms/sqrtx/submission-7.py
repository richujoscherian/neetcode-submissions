class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        ans=0
        while l*l<=x:
            ans=l
            l+=1
            

        return ans

