class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count=Counter(chars)
        res=0

        for i in words:
            good=True
            checker=Counter(i)

            for j in checker.keys():
                if checker[j]>count[j]:
                    good=False
            if good:
                res+=len(i)        
        return res        


