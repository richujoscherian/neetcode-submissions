class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res=len(text)
        counttext=Counter(text)
        countballoon=Counter("balloon")


        for i in countballoon:
            res=min(res,counttext[i]//countballoon[i])
        return res    
