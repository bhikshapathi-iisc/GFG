#User function Template for python3
class Solution:
    def setMatrixZeroes(self, matrix):
        m= len(matrix)
        n=len(matrix[0])
        c=0
        for i in range(m):
          if matrix[i][0]==0:
            c=1
          for j in range(1,n):
            if matrix[i][j]==0:
                matrix[0][j]=0
                matrix[i][0]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if matrix[0][0]==0:
            for j in range(n):
                matrix[0][j]=0
        if c==1:
            for i in range(m):
                matrix[i][0]=0
