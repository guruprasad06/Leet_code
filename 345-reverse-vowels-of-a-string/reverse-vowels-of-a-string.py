class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        l=[]
        j=[]

        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                l.append(s[i])
                j.append(i)
        l=l[::-1]
        print(l)

        for i in range(len(l)):
            s[j[i]]=l[i]
        return "".join(s)