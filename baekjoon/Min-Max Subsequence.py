n=int(input())
arr=list(map(int,input().split()))


minimum=min(arr)
maximum=max(arr)

result=len(arr)

if minimum==maximum:
    result=1
else:
    count=0
    what_caught=None
    for i in range(len(arr)):
        if what_caught==None:
            if arr[i]==minimum:
                what_caught='min'
                count+=1
            elif arr[i]==maximum:
                what_caught='max'
                count+=1

        elif what_caught=='min':
            count+=1
            if arr[i]==minimum:
                count=1
            elif arr[i]==maximum:
                if result>count:
                    result=count
                what_caught='max'
                count=1
        elif what_caught=='max':
            count+=1
            if arr[i]==minimum:
                if result>count:
                    result=count
                what_caught='min'
                count=1
            elif arr[i]==maximum:
                count=1



print(result)