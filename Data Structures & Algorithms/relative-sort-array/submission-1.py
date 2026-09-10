class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res=[]
        for i in arr2:
            for index,j in enumerate(arr1):
                if j==i:
                    res.append(j)
                    arr1[index]=-1

        arr1.sort()
        for i in range(len(res),len(arr1)):
            res.append(arr1[i])
        return res    
               
