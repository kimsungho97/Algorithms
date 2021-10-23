def left_rot(arr):
    if(len(arr)>0):
        temp=arr[0]
        del arr[0]
        arr.append(temp)
        return arr

def right_rot(arr):
    if(len(arr)>0):
        temp=arr[-1]
        del arr[-1]
        arr=[temp]+arr
        return arr

def q_remove(arr):
    if(len(arr)>0):
        return arr[1:]

def get_loc(arr, n):
    for i in range(len(arr)):
        if(arr[i]==n):
            return i

        
length, n=map(int,input().split())
arr=list(map(int,input().split()))
queue=[i for i in range(1,length+1)]
count=0

for i in range(n):
    loc=get_loc(queue,arr[i])
    if(loc>len(queue)/2):
        while(queue[0]!=arr[i]):
            count+=1
            queue=right_rot(queue)
    else:
        while(queue[0]!=arr[i]):
            count+=1
            queue=left_rot(queue)
    
    queue=q_remove(queue)

print(count)
