print "enter the size of the matrix"
n=int(input())
matrix=[]
for i in range(0,n):
    print "enter the elements of row no.", i
    matrix.append([int(x) for x in raw_input().split()])
k = 0; l = 0
while (k < n and l < n) :
    for i in range(l, n) :
        print(matrix[k][i])
    k += 1
    for i in range(k, n) :
        print(matrix[i][n - 1])
    n -= 1
    if ( k < n) :
        for i in range(n - 1, (l - 1), -1) :
            print(matrix[n - 1][i])
    n -= 1
    if (l < n) :
        for i in range(n - 1, k - 1, -1) :
            print(matrix[i][l])
    l += 1
 

 