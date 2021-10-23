n = int(input())

nums = [int(input()) for i in range(n)]
nums.reverse()
result = []

arr = [i for i in range(n, 0, -1)]
stack = []
while(len(nums) > 0):
    if(len(stack) == 0):
        stack.append(arr.pop())
        result.append("+")
    else:
        while(stack[-1] != nums[-1] and len(arr) > 0):
            stack.append(arr.pop())
            result.append("+")
        if(len(arr) == 0 and stack[-1] != nums[-1]):
            break
        elif(stack[-1] == nums[-1]):
            nums.pop()
            stack.pop()
            result.append("-")

if(len(stack) != 0):
    print("NO")
else:
    print('\n'.join(result))
