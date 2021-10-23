num, length=list(map(int,input().split()))

arr=list(range(1,num+1))

for i in range(2**num-1,0,-1):
    b=str(format(i,'b'))
    b='0'*(num-len(b))+b
    b=list(b)
    if(b.count('1')!=length):
        continue
    else:
        temp=[]
        for j in range(num):
            if(b[j]=='1'):
               temp.append(arr[j]) 
        print(' '.join(list(map(str,temp))))