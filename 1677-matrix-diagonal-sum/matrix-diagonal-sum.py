class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # pseduo code
        # iterate i to m
        # iterate j to n
        # when i == j : addition
        # 11 - 14
        # 22 - 23 
        # 33 - 32
        # 44 - 41
        cnt = 0
        val = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j:
                    cnt +=mat[i][j]
                    val.append((i,j))
            if (i,len(mat)-i-1) not in val:
                cnt += mat[i][len(mat)-i-1]
        
        return cnt