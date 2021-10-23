#https://www.acmicpc.net/problem/2480
arr=list(map(int,input().split()))

count=[0 for i in range(6)]

for i in arr:
    count[i-1]+=1

if(max(count)==3):
    print(10000+(count.index(max(count))+1)*1000)
elif(max(count)==2):
    print(1000+(count.index(max(count))+1)*100)
else:
    print(max(arr)*100)