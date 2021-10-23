def solution(n, k, cmd):
    selected=k
    
    deleted=[]
    table=[i for i in range(n)]
    temp=table[selected]
    record=[]
    record.append(table.copy())
    answer=''

    for c in cmd:
        command=c.split()
        #위로 X행 
        if command[0]=='U':
            selected-=int(command[1])
            temp=table[selected]
        #아래로 X행
        elif command[0]=='D':
            selected+=int(command[1])
            temp=table[selected]
        #삭제
        elif command[0]=='C':
            record.append(table.copy())
            del table[selected]
            if selected>=len(table):
                selected=len(table)-1
            temp=table[selected]
        #삭제취소
        elif command[0]=='Z':
            table=record.pop()
            selected=table.index(temp)
        #print(c)
        #print(table,selected)
        #print(record)
    index=0
    current=table[index]
    temp=len(table)-1
    for i in range(n):
        if current==i:
            answer+='O'
            index+=1
            if temp>=index:
                current=table[index]
            else:
                answer+='X'*(n-current-1)
                break
        else:
            answer+='X'
    return answer

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))