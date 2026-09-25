class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d={}
        for i in nums1:
            if i in nums2:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
        print(d)
        return list(d)