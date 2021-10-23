num, length= list(map(int,input().split()))

arr=list(map(int,input().split()))
temp=[0 for i in range(length)]
result=[]
temp_arr=[]

def solution(length, arr, temp_arr):
    global result
    if(length==0):
        result=[]
    if(len(temp_arr)==0):
        k=arr.copy()
        for i in arr:
            solution(length,k,[i])
            k.remove(i)
    elif(len(temp_arr)==length):
        result.append(sorted(temp_arr))
    elif(len(temp_arr)!=length):
        k=arr.copy()
        for i in arr[:]:
            solution(length,k,temp_arr+[i])
            k.remove(i)

    
solution(length,arr,result)
result.sort()
for i in result:
    print(" ".join(list(map(str,i))))

