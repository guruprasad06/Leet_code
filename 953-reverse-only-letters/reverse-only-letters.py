class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l=[]

        for i in s:
            if i.isalpha():
                l.append(i)
        l=l[::-1]
        s=list(s)
        j=0
        for i in range(len(s)):
            if s[i].isalpha():
                s[i]=l[j]
                j+=1
        return "".join(s)