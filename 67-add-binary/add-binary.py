class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=int(a,2)
        j=int(b,2)
        Sum=i+j
        print(Sum)
        res=bin(Sum)
        print(res)
        return res[2:]