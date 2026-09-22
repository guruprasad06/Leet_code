class Solution(object):
    def firstUniqChar(self, s):
        l=[0]*26
        for i in s:
            j=ord(i)-97
            l[j]+=1
        for i in range(len(s)):
            if l[ord(s[i])-97]==1:
                return i
        return -1
        