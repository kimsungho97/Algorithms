#덩치(브루트포스)

a=list()
n=int(input())

for i in range(0,n):
    a.append(list(map(int,input().split(" "))))

score=list()

for p in range(0,len(a)):
    k=1
    for j in range(0,len(a)):
        if p==j: continue
        else:
            if a[p][0]<a[j][0] and a[p][1]<a[j][1]:
                k+=1
    score.append(k)

print(" ".join(list(map(str,score))))