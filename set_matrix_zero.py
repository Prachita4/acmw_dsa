def set_zero(mat, m, n):
    for i in range(len(mat[0])):
        mat[m][i]=0
    for i in range(len(mat)):
        mat[i][n]=0
    return mat

def main():
    print("Enter number of rows and columns")
    m=int(input())
    n=int(input())
    zero_positions=[]
    mat=[]
    
    print("Enter matrix elements")
    for i in range(m):
        row=[]
        for j in range(n):
            ele=int(input())
            row.append(ele)
        mat.append(row)
    print(mat)
    for i in range(m):
        for j in range(n):
            if mat[i][j]==0:
                zero_positions.append([i,j])
            else:
                pass
    for i,j in zero_positions:
        mat=set_zero(mat,i,j)
    print(mat)

main()
