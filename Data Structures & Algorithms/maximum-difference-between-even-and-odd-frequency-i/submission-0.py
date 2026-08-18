class Solution:
    def maxDifference(self, s: str) -> int:
        dict1={}
 
        for i in s:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        even=[]
        odd=[]        
        for key,value in dict1.items():
            if value%2==0:
                even.append(value)
            else:
                odd.append(value)
        a1=max(odd)        
        a2=min(even)

        diff=a1-a2
        return diff  


