def diagonalDifference(arr,n) :
    sum1=0
    sum2=0
    for i in range (n):
        for j in range (n):
            if(i==j):
                sum1+=arr[i][j]
            elif(i+j==2):
                sum2+=arr[i][j]
    diff=abs(sum1-sum2)
    return diff

arr=[[11,2,4],
[4,5,6],
[10,8,-12]]
print(diagonalDifference(arr,3)

