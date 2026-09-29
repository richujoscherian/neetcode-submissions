class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        i=0
        while i<len(nums):
            j=i

            while j<len(nums) and nums[j]==nums[i]:
                j+=1
            if (j-i)%2!=0:
                return False
            i=j    
        return True            
            