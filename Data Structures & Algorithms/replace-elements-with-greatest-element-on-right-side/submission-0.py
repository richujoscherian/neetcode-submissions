class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        RightMax=-1

        for i in range(len(arr)-1,-1,-1):
            NewMax=max(RightMax,arr[i])
            arr[i]=RightMax
            RightMax=NewMax
        return arr    