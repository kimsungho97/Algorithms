#https://www.acmicpc.net/problem/16675

#승패를 알려주는 함수
def who_is_winner(M,R):
    if M=='R':
        if R=='R':
            return 0
        elif R=='S':
            return -1
        else:
            return 1
    elif M=='S':
        if R=='R':
            return 1
        elif R=='S':
            return 0
        else:
            return -1
    else:
        if R=='R':
            return -1
        elif R=='S':
            return 1
        else:
            return 0

line=list(input().split())

result=[]

result.append(who_is_winner(line[0],line[2]))
result.append(who_is_winner(line[0],line[3]))
result.append(who_is_winner(line[1],line[2]))
result.append(who_is_winner(line[1],line[3]))
is_checked=False
for i in range(3):
    if(is_checked==True):
        break
    for j in range(i+1,4):
        if i==0 and j==3:
            continue
        elif i==1 and j==2:
            continue

        temp=result[i]+result[j]

        if((i==0 and j==1) or (i==2 and j==3)) and (temp==-2):
            print("MS")
            is_checked=True
            break
        elif((i==0 and j==2) or (i==1 and j==3)) and (temp==2):
            print("TK")
            is_checked=True
            break
if not is_checked:
    print("?")
