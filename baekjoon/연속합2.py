n=int(input())
arr=list(map(int,input().split()))

 sum_arr=[[-99999 for j in range(len(arr))] for i in range(len(arr))]

 for i in range(len(arr)):
     if(i==0):
         sum_arr[0]=arr.copy()
    else:
        for j in range(len(arr)):
            if(sum_arr[i-1][j]+sum_arr[i-1])
            sum_arr[i][j]=
