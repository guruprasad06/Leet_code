class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        print(d)
        sum=0
        flag=0
        for i in d:
            if d[i]%2==0:
                sum+=d[i]
            else:
                sum+=d[i]-1
                flag=1
        if flag==1:
            sum+=1
        return sum
        
