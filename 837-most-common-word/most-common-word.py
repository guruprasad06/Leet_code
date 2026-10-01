class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:

        #   
        paragraph=paragraph.lower()
        print(paragraph)
        ans=""
        for i in paragraph:
            if i==" "or i.isalnum():
                ans+=i
            else:
                ans+=" "
        print(ans)

        l=ans.split()

        d={}
        for i in l:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        print(d)

        sor=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
        print(sor)

        for i in sor:
            if i not in banned:
                return (i)
            
            
    
    
    
    
    
# sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True)