class Solution:
    def countSeniors(self, details: List[str]) -> int:
        output=0
        for i in details:
            if int(i[11:13])>60:
                output+=1
        return output        