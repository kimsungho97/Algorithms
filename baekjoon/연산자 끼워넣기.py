n=int(input())
nums=list(map(int,input().split()))
op=list(map(int,input().split()))
op_signs=['+','-','*','/']


#결과로 나올 최대, 최소값
max_result=-1000000000
min_result=1000000000

#nums: 입력받은 숫자들
#cur_index: 현재까지 계산한 위치
#op : 사용하지 않은 연산자
#cur_result: 계산된 값
def calculate(nums, cur_index, op, cur_result):
    global max_result, min_result
    global n

    #모든 숫자의 계산이 완료되었을 때 최대, 최소 비교후 대입
    if cur_index == n-1:
        if max_result < cur_result:
            max_result = cur_result
        if min_result > cur_result:
            min_result = cur_result
        return
    
    else:
        for i in range(len(op)):
            if op[i]<=0:
                continue
            else:
                op_copy=op.copy()
                op_copy[i]-=1
                if i==0:    #덧셈
                    calculate(nums, cur_index+1, op_copy, cur_result+nums[cur_index+1])
                elif i==1:  #뺄셈
                    calculate(nums, cur_index+1, op_copy, cur_result-nums[cur_index+1])
                elif i==2:  #곱셈
                    calculate(nums, cur_index+1, op_copy, cur_result*nums[cur_index+1])
                elif i==3:  #나눗셈
                    calculate(nums, cur_index+1, op_copy, int(cur_result/nums[cur_index+1]))


calculate(nums, 0, op, nums[0])

print(max_result)
print(min_result)




