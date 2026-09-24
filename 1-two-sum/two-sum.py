class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d={}
        for i in range(len(nums)):
            left =target-nums[i]
            if left in d:
                return [i,d[left]]
            d[nums[i]]=i

