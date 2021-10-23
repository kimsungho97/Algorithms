import math

def get(arr):
    [x1,y1,r1,x2,y2,r2]=arr
    d=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if x1==x2 and y1==y2 and r1==r2:
        return -1
    elif d>r1+r2:
        return 0
    elif d<abs(r1-r2):
        return 0
    elif d==0 and r1!=r2:
        return 0
    elif d==r1+r2:
        return 1
    elif d==abs(r1-r2):
        return 1
    elif d<r1+r2 and d>abs(r1-r2):
        return 2
    

n=int(input())



for i in range(0,n):
    arr=list(map(int,input().split(" ")))
    print(get(arr))