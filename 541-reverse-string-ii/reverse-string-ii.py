class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i=0
        ans=""

        while i<len(s)-k:
            t=s[i:i+k][::-1]
            ans=ans+t
            ans=ans+s[i+k:i+2*k]
            i=i+2*k
        ans=ans+s[i:][::-1]
        return ans