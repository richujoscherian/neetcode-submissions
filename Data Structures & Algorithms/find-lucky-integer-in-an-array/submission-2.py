class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count={}

        for i in arr:
            count[i]=count.get(i,0)+1
        magic=[]
        maximum=-1
        for j in count:
            if count[j]==j:
                magic.append(j)
        if magic:
            return max(magic)
        return -1    
