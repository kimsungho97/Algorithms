n=int(input())


for i in range(0,n):
    k=[i]+list(map(int,list(str(i))))
    if sum(k)==n:
        print(i)
        break
    if(i==n-1):
        print(0)
    