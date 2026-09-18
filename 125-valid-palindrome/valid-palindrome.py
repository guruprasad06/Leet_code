class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for i in s:
            if i.isalnum():
                ans=ans+i.lower()
        print(ans)
        print(ans[::-1])
        return ans==ans[::-1]