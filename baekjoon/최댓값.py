nums=[int(input()) for i in range(9)]
print(max(nums))
for i in range(9):
    if(nums[i]==max(nums)):
        print(i+1)


