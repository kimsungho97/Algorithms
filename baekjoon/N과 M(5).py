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
        for i in arr:
            k=arr.copy()
            k.remove(i)
            solution(length,k,[i])
    elif(len(temp_arr)==length):
        result.append(temp_arr)
    elif(len(temp_arr)!=length):
        for i in arr[:]:
            k=arr.copy()
            k.remove(i)
            solution(length,k,temp_arr+[i])

    
solution(length,arr,result)
result.sort()
for i in result:
    print(" ".join(list(map(str,i))))

