class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        res=[]

        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        
        
        for num , freq in count.items():
            if freq > len(nums)//3:
                res.append(num)

        return res                  
            
