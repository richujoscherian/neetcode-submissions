class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        # checking s to t
        for i in range(len(s)):
            if s[i] not in dict1.keys():
                dict1[s[i]]=t[i]
            else:
                if dict1[s[i]]!=t[i]:
                    return False
        # checking t to s
            if t[i] not in dict2.keys():
                dict2[t[i]]=s[i]
            else:
                if dict2[t[i]]!=s[i]:
                    return False          
        return True       