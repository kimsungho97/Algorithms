num, length= list(map(int,input().split()))

arr=sorted(list(map(int,input().split())))
temp=[0 for i in range(length)]
result=[]
temp_arr=[]

def solution(length, arr, temp_arr):
    global result
    if(length==0):
        result=[]
    if(len(temp_arr)==0):
        k=sorted(arr.copy())
        for i in sorted(list(set(arr))):
            for j in range(len(k)):
                if k[j]==i:
                    del k[j]
                    break
            solution(length,k,[i])
    elif(len(temp_arr)==length):
        temp_arr.sort()
        if not temp_arr in result:
            result.append(temp_arr)
    elif(len(temp_arr)!=length):
        k=sorted(arr.copy())
        for i in sorted(list(set(arr))):
            for j in range(len(k)):
                if k[j]==i:
                    del k[j]
                    break
            solution(length,k,temp_arr+[i])

    
solution(length,arr,result)


result.sort()
for i in result:
    print(" ".join(list(map(str,i))))

