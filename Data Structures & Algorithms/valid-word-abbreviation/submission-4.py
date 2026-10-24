class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        len1=len(word)
        len2=len(abbr)
        l,r=0,0

        while l<len1 and r<len2:
            if abbr[r]=="0":
                return False
            if word[l]==abbr[r]:
                l+=1
                r+=1
            elif abbr[r].isalpha():
                return False
            else:
                sublen=0
                while r<len2 and abbr[r].isdigit():

                    sublen=sublen*10+int(abbr[r])
                    r+=1
                l+=sublen
        return l==len1 and r==len2
            
                
            
            
