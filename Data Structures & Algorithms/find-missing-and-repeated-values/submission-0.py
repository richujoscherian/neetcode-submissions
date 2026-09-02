class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        count={}
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] not in count:
                    count[grid[i][j]]=0
                count[grid[i][j]] +=1
        double,missing=0,0
        for i in range (1,n*n +1):
            if i not in count:
                missing=i
            elif count[i]==2:
                double=i    
        return [double,missing]        

