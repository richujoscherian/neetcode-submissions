class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current=nums[0]
        maximum=nums[0]

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                current+=nums[i]
                if maximum<current:
                    maximum=current
            else:
                current=nums[i]    
        return maximum        
