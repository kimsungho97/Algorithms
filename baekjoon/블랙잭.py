[n,m]=list(map(int,input().split()))
arr=list(map(int,input().split()))

new_arr=[sum([arr[i],arr[j],arr[k]]) for i in range(0,len(arr)-2) for j in range(i+1,len(arr)-1) for k in range(j+1,len(arr))]

new_arr.sort()

for i in range(len(new_arr)-1,0,-1):
    if(new_arr[i]<=m):
        print(new_arr[i])
        break