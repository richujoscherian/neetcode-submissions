class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels={"a","e","i","o","u"}
        vowelwords=[]
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                vowelwords.append(1)
            else:
                vowelwords.append(0)
        result=[]
        for value in queries:
            left=value[0]
            right=value[1]
            new=0
            for i in range(left,right+1):
                new+=vowelwords[i]
            result.append(new)
        return result    

                


            
