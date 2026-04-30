class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        Maxcount,res=0,0

        for num in nums:
            count[num]=1+count.get(num,0)

            if count[num]>Maxcount:
                res=num
                Maxcount=count[num]

        return res      