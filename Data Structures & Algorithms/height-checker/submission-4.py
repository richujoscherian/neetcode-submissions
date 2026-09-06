class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=[0]*101
        for h in heights: 
            count[h]+=1
        expected=[]
        for h in range(len(count)):
            if count[h] >= 1:#unnecessary step
                for i in range(count[h]):
                    expected.append(h)
        result=0            
        for i in range(len(heights)):
            if heights[i]!=expected[i]:
                result+=1
        return result        


