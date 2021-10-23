#https://www.acmicpc.net/problem/16676

n=int(input())


length=len(str(n))
m=n-1
k=str(n)[0]
if int(k)>1:
    print(length)
else:
    temp=int(k*length)
    if temp<=n:
        print(length)
    else:
        print(length-1)





