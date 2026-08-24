class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for i in nums1:
            maxvalue=-1
            for j in range(len(nums2)-1,-1,-1):
                if nums2[j]>i:
                    maxvalue=nums2[j]
                if nums2[j]==i:
                    break
            result.append(maxvalue)
        return result        

                