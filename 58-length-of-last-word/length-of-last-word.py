class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i=len(s)-1
        while s[i]==" ":
            i-=1
        c=0
        while i>-1 and s[i]!=" ":
            c+=1
            i-=1
        return c
