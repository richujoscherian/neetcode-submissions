class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        list1=[]
        maxvalue=0
        for i in range(len(nums)-1):
            
            if nums[i+1]>nums[i]:
                maxvalue+=nums[i]

            else:
                maxvalue+=nums[i]    
                list1.append(maxvalue)
                maxvalue=0
        maxvalue+=nums[-1]
        list1.append(maxvalue)    



        return max(list1)        
