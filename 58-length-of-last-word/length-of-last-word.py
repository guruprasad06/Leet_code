class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)-1
        print(i)
        while s[i]==" ":
            i-=1
        print(i)
        c=0
        while s[i]!=" " and i>-1:
            c+=1
            i-=1
        return c
        
        
        