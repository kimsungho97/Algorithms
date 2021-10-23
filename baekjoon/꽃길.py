#https://www.acmicpc.net/problem/14620

n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

index=list(range(1,n-1))

ans=10**10

def calc_price(arr,r,c):
    result=0
    result+=arr[r][c]
    result+=arr[r-1][c]
    result+=arr[r+1][c]
    result+=arr[r][c+1]
    result+=arr[r][c-1]
    return result
    

def backtracking(arr,n,index,cur_ans,cur_index):
    global ans
    if len(cur_index)==3:
        if ans>cur_ans:
            #print(cur_index)
            ans=cur_ans
    
    elif not(ans<=cur_ans):
        if len(cur_index)==0:
            for r in index:
                for c in index:
                    backtracking(arr,n,index,calc_price(arr,r,c),[[r,c]])
        else:
            temp=cur_index[-1]
            for r in range(1,n-1):
                for c in range(1,n-1):
                    is_possible=True
                    for k in cur_index:
                        if abs(r-k[0])<=2 and c==k[1]:
                            is_possible=False
                            break
                        elif abs(c-k[1])<=2 and r==k[0]:
                            is_possible=False
                            break
                        elif abs(r-k[0])==1 and abs(c-k[1])==1:
                            is_possible=False
                            break
                    if is_possible:
                        cur_index_temp=cur_index.copy()
                        cur_index_temp.append([r,c])
                        backtracking(arr,n,index,cur_ans+calc_price(arr,r,c),cur_index_temp)

backtracking(arr,n,index,0,[])
print(ans)
        
        

