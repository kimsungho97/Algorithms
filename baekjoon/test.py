k=int(input())

for i in range(0,k):
    arr=list(map(int,input().split(" ")))
    for j in range (0,10):
        if arr[j]!=j%5+1:
            break
        if j==9:
            print(i+1)    