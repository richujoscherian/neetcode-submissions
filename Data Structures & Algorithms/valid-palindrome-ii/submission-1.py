class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1

        while l<r:
            if s[l]!=s[r]:
                lskip,rskip=s[l+1:r+1],s[l:r]
                return (lskip==lskip[::-1]) or (rskip==rskip[::-1])
            l+=1
            r-=1
        return True