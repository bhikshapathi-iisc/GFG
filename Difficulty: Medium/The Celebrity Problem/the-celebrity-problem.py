class Solution:
    def celebrity(self, mat):
        # code here
        n=len(mat)
        a,b=0,n-1
        while a<b:
            if mat[a][b]==1:
                a+=1
            else:
             b-=1
        for i in range(n):
            if i !=a:
                if mat[a][i]==1 or mat[i][a]==0:
                    return -1
        return a
        