class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        l=[]
        for i in nums1:
            if i in nums2:
                if i not in l:
                    l.append(i)
        return l