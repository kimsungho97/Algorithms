#https://www.acmicpc.net/problem/16143

import numpy as np

n=int(input())
line=""
for i in range (0,n):
    line+=input()
    if i!=n-1:
        line+=";"
    
matrix=np.matrix(line)
matrix2=matrix
sum=matrix
nozero=False
k=1

for i in range(0,n):
    nozero=False
    for j in range(0,n):
        if nozero:
            break
        for l in range(0,n):
            if sum[j,l]==0:
                nozero=True
                break
            if j==n-1 and l==n-1 and nozero==False:
                print(k)
                exit()

    sum+=np.dot(matrix2,matrix)
    matrix2=np.dot(matrix2,matrix)
    k+=1

print(0)