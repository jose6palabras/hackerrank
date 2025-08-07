'''You are provided with a matrix grid of size m x n, where each cell contains a positive integer. 
You can move from any cell in the grid to another cell that is either directly below or to the 
right of it (the cells don't have to be adjacent). The score of a move from a cell with value
c1 to a cell with value c2 is calculated as c2-c1. 
You can begin at any cell in the matrix, but you must make at least one move. 
Your task is to determine the maximum possible total score you can achieve.'''
#plan
'''
Idea: take each cell and look to the botton of right if there is a number grater than it. If yes from
the new grater look for other grater and so on until create a path step.
1. function that takes a cell and returns 
'''

matrix_s = [[4,3,2], [3,2,1]]
def minimum(matrix, i_p, j_p):
    minimum = float('inf')
    for i in range(0, i_p+1):
        if min(matrix[i][:j_p+1])<minimum:
            minimum = min(matrix[i][:j_p+1])
    return minimum
def maximum(matrix):
    maximun_n = float('-inf')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i!=0 and j!=0:
                if maximun_n < matrix[i][j]:
                    maximun_n = matrix[i][j]
                    i_p, j_p = i, j
    minimum_n = minimum(matrix, i_p, j_p)
    return maximun_n - minimum_n
print(maximum(matrix_s))


