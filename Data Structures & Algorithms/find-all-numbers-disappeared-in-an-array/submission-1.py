class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)

        for num in nums:
            index=abs(num)-1
            nums[index]=-abs(nums[index])

        output=[]

        for i in range(n):
            if nums[i]>0:
                output.append(i+1)
        return output 
