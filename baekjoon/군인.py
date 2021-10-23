#https://www.acmicpc.net/problem/1321

def get(arr,num):
    left, right=0,len(arr)-1
    while True:
        if right-left<5:
            for i in range(left,right+1):
                if arr[i]>num:
                    return i+1
        mid=(left+right)/2
        if arr[mid]>num:
            right=mid
        elif arr[mid]<num:
            left=mid
        else:
            return mid+1


n=int(input())
num=list(map(int,input().split(" ")))
for i in range(1,n):
    num[i]=num[i-1]+num[i]

n=int(input())

for i in range(0,n):
    line=input().split(" ")
    if line[0]=='1':
        num[int(line[1])-1]+=int(line[2])
    else:
        print(get(num,int(line[1])))