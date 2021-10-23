
n=int(input())

for i in range(n):
    answer=True
    v,e=list(map(int,input().split()))
    sets=[[]for i in range(v)]
    st=[]
    color=[0 for i in range(v)]
    for j in range(e):
        a,b=list(map(int,input().split()))
        sets[a-1].append(b-1)
        sets[b-1].append(a-1)

    st.append(0)
    nowcolor=1
    color[0]=nowcolor
    while(len(st)!=0):
        now=st[0]
        del st[0]
        if(nowcolor==1):
            nowcolor=2
        else:
            nowcolor=1

        for k in sets[now]:
            if(answer==False):
                break
            elif(color[k]==0):
                color[k]=nowcolor
                st.append(k)
            elif(color[k]!=0): 
                for another in sets[k]:
                    if(color[another]==color[k]):
                        answer=False
                        break

    if answer:
        print("YES")
    else:
        print("NO")    

    