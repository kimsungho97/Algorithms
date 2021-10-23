#https://www.acmicpc.net/problem/14225
n=int(input())
arr=list(map(int,input().split()))

#부분 합으로 만들 수 있는 숫자들 모음
enable=[]
enable.append(0)

for num in arr:
    temp=enable.copy()
    for e in enable:
        temp.append(e+num)
    temp.append(num)
    enable=temp

#없는 숫자 1부터 확인
enable.sort()
enable.remove(0)
current_num=1
while True:
    if len(enable)==0:
        print(current_num)
        break
    if enable[0]==current_num:
        while len(enable)!=0 and enable[0]==current_num:
            del enable[0]
        current_num+=1
    else:
        print(current_num)
        break