#User function Template for python3

def rotate(matrix): 
    #code here
        n=len(matrix)
        res=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[j][n-i-1]=matrix[i][j]
        for i in range(n):
            for j in range(n):
              matrix[i][j]=res[i][j]