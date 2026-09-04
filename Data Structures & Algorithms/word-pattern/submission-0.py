class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterntoword={}
        wordtopattern={}
        list1=s.split()

        if len(pattern)!=len(list1):
            return False

        for i in range(len(pattern)):
            c=pattern[i]
            w=list1[i]

            if c in patterntoword:
                if patterntoword[c]!=w:
                    return False
            if w in wordtopattern:
                if wordtopattern[w]!=c:
                    return False
            patterntoword[c]=w
            wordtopattern[w]=c
        return True                    
