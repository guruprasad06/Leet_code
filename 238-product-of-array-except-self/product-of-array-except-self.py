class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        p=1
        for i in nums:
            l.append(p)
            p=p*i        

        r=[]
        p=1
        for i in range(len(nums)-1,-1,-1):
            r.append(p)
            p=p*nums[i]
        r=r[::-1]
        ans=[]

        for i in range(len(nums)):
            ans.append(l[i]*r[i])
        return ans