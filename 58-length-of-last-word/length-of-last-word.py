class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=s.split()
        print(n[-1])
        return len(n[-1])
