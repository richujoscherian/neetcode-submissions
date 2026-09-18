class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output=[]
        for i in nums:
            output.append(i**2)
        output.sort()
        return output        