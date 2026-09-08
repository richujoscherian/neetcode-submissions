class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        for i in range(1,len(nums)):
            div1=nums[i]%2
            div2=nums[i-1]%2
            if div1==div2:
                return False
        return True        

