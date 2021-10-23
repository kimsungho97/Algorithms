#https://www.acmicpc.net/problem/11066

n=int(input())

result=[]
total=0

def get_min(num,dynamic,cur):
    temp=dynamic[cur[0]][cur[0]]+dynamic[cur[0]+1][cur[1]]
    first=(cur[0],cur[0])
    second=(cur[0]+1,cur[1])
    for i in range(1,cur[1]-cur[0]):
        k=dynamic[cur[0]][cur[0]+i-1]+dynamic[cur[0]+i][cur[1]]
        if temp>k:
            temp=k
            first=(cur[0],cur[0]+i-1)
            second=(cur[0]+i,cur[1])
    return first,second

def get_total(arr,num,path,dynamic,cur):
    global total
    first=None
    second=None
    #if cur==(0,num-1):
    first,second=get_min(num,dynamic,cur)
    #else:
    #    first=(path[cur[0]][cur[1]][0],path[cur[0]][cur[1]][1])
    #    second=(path[cur[0]][cur[1]][2],path[cur[0]][cur[1]][3])
    if first[0]!=first[1]:
        get_total(arr,num,path,dynamic,first)
    if second[0]!=second[1]:
        get_total(arr,num,path,dynamic,second)

    total+=dynamic[cur[0]][cur[1]]

for _ in range(n):
    num=int(input())
    arr=list(map(int,input().split()))
    total=0
    #dp
    dynamic=[]
    path=[]
    for i in range(num):
        dynamic.append([10000 for j in range(num)])
        path.append([[() for l in range(num)] for j in range(num)])

    for i in range(num):
        for j in range(num-i):
            if(i==0):
                dynamic[j][j]=arr[j]
            else:
                for k in range(1,i+1):
                    temp=dynamic[j][i+j-k]+dynamic[i+j-k+1][i+j]
                    if j!=(i+j-k):
                        temp+=dynamic[j][i+j-k]
                        if(path[j][i+j-k][0]!=path[j][i+j-k][1]):
                            temp-=dynamic[path[j][i+j-k][0]][path[j][i+j-k][1]]
                        if(path[j][i+j-k][2]!=path[j][i+j-k][3]):
                            temp-=dynamic[path[j][i+j-k][2]][path[j][i+j-k][3]]
                    if (i+j-k+1)!=(i+j):
                        temp+=dynamic[i+j-k+1][i+j]
                        if(path[i+j-k+1][i+j][0]!=path[i+j-k+1][i+j][1]):
                            temp-=dynamic[path[i+j-k+1][i+j][0]][path[i+j-k+1][i+j][1]]
                        if(path[i+j-k+1][i+j][2]!=path[i+j-k+1][i+j][3]):
                            temp-=dynamic[path[i+j-k+1][i+j][2]][path[i+j-k+1][i+j][3]]
                    if dynamic[j][i+j]>temp:
                        dynamic[j][i+j]=temp
                        path[j][i+j]=(j,i+j-k,i+j-k+1,i+j)
    
    #print(sum(arr))
    #for i in dinamic:
    #    print(i)
    #print(dinamic[0][num-1]+dinamic[path[0][num-1][0]][path[0][num-1][1]]+dinamic[path[0][num-1][2]][path[0][num-1][3]])
    #get_total(arr,num,path,dynamic,(0,num-1))
    result.append(dynamic[0][num-1])
    #print(dynamic[0][num-1])
    




for i in result:
    print(i)

