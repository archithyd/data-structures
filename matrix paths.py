def path(matrix,n):
    i=0
    j=0
    k=0
    x=0
    while(k<n):
        if(matrix[i+1][j]==1 and i+1<n):
            x=i+1
            print(x,j)
        if(matrix[i][j+1]==1 and j+1<n):
            x=j+1
            print(i,x)
        k+=1


mat=[[1,0],[1,1]]
path(mat,2)



