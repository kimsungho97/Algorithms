#https://www.acmicpc.net/problem/10653
import math
import itertools

line=input()
n=int(line.split(" ")[0])
k=int(line.split(" ")[1])

points=[]

def gettotal(tmp):
    arr=list(tmp)
    k=len(arr)
    sum=0
    for i in range(0,k-1):
        x1=arr[i][0]
        y1=arr[i][1]
        x2=arr[i+1][0]
        y2=arr[i+1][1]
        length=abs(x1-x2)+abs(y1-y2)
        sum+=length
    return sum

for i in range(0,n):
    line=input()
    points.append([int(line.split(" ")[0]),int(line.split(" ")[1])])


tmp=[]
l=len(list(itertools.combinations(points[1:-1],n-k-2)))
total=(gettotal((list([points[0]])+list(list(itertools.combinations(points[1:-1],n-k-2))[0])+list([points[-1]]))))
for i in range(1,l):
    t=gettotal((list([points[0]])+list(list(itertools.combinations(points[1:-1],n-k-2))[i])+list([points[-1]])))
    if total>t:
        total=t

print(total)

