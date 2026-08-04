class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # unique=set()
        # for e in emails:
        #     local,domain=e.split("@")
        #     local=local.split("+")[0]
        #     local=local.replace(".","")
        #     unique.add((local,domain))
        # return len(unique)

        unique=set()
 
        for e in emails:
            local,domain="",""
            i=0
            while e[i] not in ['+','@']:
                if e[i]=='.':
                    i+=1

                local+=e[i]
                i+=1
            while e[i]!="@":
                i+=1
            domain=e[i+1:]    
            unique.add((local,domain))     
        return len(unique)       
