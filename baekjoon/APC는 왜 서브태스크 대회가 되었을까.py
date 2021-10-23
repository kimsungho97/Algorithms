#https://www.acmicpc.net/problem/17224

n,l,k=list(map(int,input().split()))

quiz=[]
for i in range(n):
    quiz.append(list(map(int,input().split())))

quiz.sort(reverse=False, key=lambda x:x[0])
quiz.sort(reverse=False, key=lambda x:x[1])

count=0
result=0

if k==0:
    print(0)
else:
    for i in quiz:
        if i[0]>l:
            continue
        elif i[0]<=l:
            result+=100
            count+=1
            if i[1]<=l:
                result+=40
        
        if count>=k:
            break

    print(result)


