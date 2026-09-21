class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        val=[]
        index=[]
        for i in range(len(s)):
            if s[i] in'aeiouAEIOU':
                val.append(s[i])
                index.append(i)
        val=val[::-1]

        for i in range(len(val)):
            s[index[i]]=val[i]
        return "".join(s)