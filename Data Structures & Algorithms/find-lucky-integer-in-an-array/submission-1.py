class Solution:
    def findLucky(self, arr: List[int]) -> int:
        magic=[]
        for i in range(len(arr)):
            count=0
            for j in range(len(arr)):
                if arr[j]==arr[i]:
                    count+=1
            if count==arr[i]:
                magic.append(arr[i])
        if magic!=[]:
            maximum=max(magic)     
            return maximum
        else:
            return -1    



