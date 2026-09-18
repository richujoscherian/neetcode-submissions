class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i,j=0,0
        g.sort()
        s.sort()
        while i<len(g):
            while j<len(s) and g[i]>s[j]:
                j+=1
            if j==len(s):
                break
            i+=1
            j+=1
        return i        

