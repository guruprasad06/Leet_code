class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        sum=0
        for i in range(len(mat)):
            sum+=mat[i][i] #00 11 22
            sum+=mat[i][len(mat)-i-1]  #02 11 20
        print(sum)
        if len(mat)%2==0:
            return sum
        else:
            return sum-mat[len(mat)//2][len(mat)//2]