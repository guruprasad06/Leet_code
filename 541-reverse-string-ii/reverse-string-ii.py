class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans=""
        i=0

        while i<len(s)-k:
            t=s[i:i+k][::-1]
            ans=ans+t
            print(ans)
            ans=ans+s[i+k:i+2*k]
            i=i+2*k
        print(ans)
        ans=ans+s[i::][::-1]
        return ans