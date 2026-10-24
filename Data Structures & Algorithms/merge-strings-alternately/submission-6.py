class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1=len(word1)
        len2=len(word2)
        i,j=0,0
        str1=[]

        while i<len1 and j<len2:
            str1+=word1[i]
            str1+=word2[j]

            i+=1
            j+=1

        str1.append(word2[j:])
        str1.append(word1[i:])
        return "".join(str1)