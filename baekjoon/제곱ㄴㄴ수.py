import math
k=list(map(int,input().split(" ")))
n1=0
count=k[1]-k[0]
arr=[]
for i in range(2,int(math.sqrt(k[1]))):
    arr.append(i**2)

for i in range(k[0],k[1]+1):
    for j in arr:
        if i<j:
            break
        else:
            if i%j==0:
                count-=1
                break

print(count)