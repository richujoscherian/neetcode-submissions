class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        maxcount,res=0,0

        for num in nums:
                count[num]=1 + count.get(num,0)
                if count[num] > maxcount:
                    res=num
                    maxcount=count[num]
        return res        
