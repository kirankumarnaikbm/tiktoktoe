def row_check(matrix):
    for i in range(3):
        k=matrix[i].count("X")
        l=matrix[i].count("O")
        if k==3 or l==3:
            if k==3:
                print("Anjali Wins")
            else:
                print("Abhinav Wins")


def diagonal_check(matrix):
    diagonal_matrix=[]
    for i in range(3):
        for j in range(3):
            if i==j:
                diagonal_matrix+=[matrix[i][j]]
    m=diagonal_matrix.count("X")
    n=diagonal_matrix.count("O")
    if m==3 or n==3:
        if m==3:
            print("Anjali Wins")
        else:
            print("Abhinav Wins")


def anti_diagonal_check(matrix):
    anti_diagonal_matrix=[]
    for i in range(3):
        for j in range(1,4):
            if i+1==j:
                anti_diagonal_matrix+=[matrix[i][-j]]
    m=anti_diagonal_matrix.count("X")
    n=anti_diagonal_matrix.count("O")
    if m==3 or n==3:
        if m==3:
            print("Anjali Wins")
        else:
            print("Abhinav Wins")


def transpose_matrix(matrix):
    matrix_a=[]
    for i in range(3):
        item=[]
        for j in range(3):
            item+=[matrix[j][i]]
        matrix_a.append(item)
    row_check(matrix_a)


matrix=[]
for i in range(3):
    a=input().split()
    matrix+=[a]
row_check(matrix)
diagonal_check(matrix)
anti_diagonal_check(matrix)
transpose_matrix(matrix)
