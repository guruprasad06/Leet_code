class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c=nums.count(0)
        k=[]
        for i in nums:
            if i != 0:
                k.append(i)
        
        for i in range(c):
            k.append(0)
        for i in range(len(nums)):
            nums[i]=k[i]