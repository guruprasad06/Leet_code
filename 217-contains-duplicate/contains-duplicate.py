class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        s=set(nums)
        S=len(s)
        if  n==S:
            return False
        else:
            return True
        