class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        # 00 11 22
        # 02 11 20
        sum=0

        for i in range(len(mat)):
            sum=sum+mat[i][i]
            sum=sum+mat[i][len(mat)-i-1]
        print(sum)
        if len(mat)%2==0:
            return sum
        else:
            return sum-mat[len(mat)//2][len(mat)//2]