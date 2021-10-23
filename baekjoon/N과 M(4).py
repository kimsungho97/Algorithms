num, length=list(map(int,input().split()))

arr=list(range(1,num+1))
temp=[0 for i in range(length)]

while(True):
    while(num in temp):
        for i in range(len(temp)-1):
            if(temp[i]>=num):
                temp[i+1]=temp[i+1]+1
                temp[i]=-1
        for j in range(2,len(temp)+1):
            if (temp[-j]==-1) :
                temp[-j]=temp[-j+1]
    if(sum(temp)>=(num-1)*length):
        break
    string=str()
    for i in temp:
        string=str(arr[i])+" "+string
    print(string)
    temp[0]+=1

print(" ".join(list(str(arr[-1])*length)))