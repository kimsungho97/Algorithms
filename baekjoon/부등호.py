#입력받을 부등호 개수
n=int(input())
#부등호 문자열
signs=input().split()

max_arr=[]
min_arr=[]

#maximum
nums=[i for i in range(0,10)]
max_arr.append(nums[-1])
nums.pop()
sequence_count=0
for sign in signs:
    if(sign=='>'):
        # > 부등호 만날시 가장 우측에 작은값 추가
        max_arr.append(nums[-1])
        nums.pop()
        sequence_count=0
    elif(sign=='<'):
        # < 부등호가 연속되면 연속된 부등호의 맨 좌측에 
        # 다음으로 작은값을 추가해야하므로 +1 해준다
        sequence_count+=1
        max_arr=max_arr[:-sequence_count]+[nums[-1]]+max_arr[-sequence_count:]
        nums.pop()


#minimum
nums=[9-i for i in range(0,10)] #역순으로 저장
min_arr.append(nums[-1])
nums.pop()
sequence_count=0
for sign in signs:
    if(sign=='>'):
        # > 부등호 만날시 연속된 부등호만큼 우측으로 밀고
        # 연속된 부등호의 가장 좌측에 작은값 추가
        sequence_count+=1
        min_arr=min_arr[:-sequence_count]+[nums[-1]]+min_arr[-sequence_count:]
        nums.pop()
    elif(sign=='<'):
        # < 부등호 만날 시 가장 우측에 다음으로 작은값 추가 
        min_arr.append(nums[-1])
        nums.pop()
        sequence_count=0


print("".join(list(map(str,max_arr))))
print("".join(list(map(str,min_arr))))

