class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum=0
        total=n*(n+1)//2
        for i in range(n):
            sum+=nums[i]
        return abs(total-sum)