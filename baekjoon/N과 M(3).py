num, length=list(map(int,input().split()))

arr=list(range(1,num+1))
temp=[0 for i in range(length)]

while(True):
    for i in range(len(temp)-1):
        if(temp[i]>=num):
            temp[i+1]+=1
            temp[i]=0
        else:
            break
    if(sum(temp)>=(num-1)*length):
        break
    string=str()
    for i in temp:
        string=str(arr[i])+" "+string
    print(string)
    temp[0]+=1

print(" ".join(list(str(arr[-1])*length)))
