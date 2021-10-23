arr = list(map(int, input().split()))

count = 0
start = [0, 0, 0]


def isEqual(arr1, arr2):
    for i in range(len(arr1)):
        if(arr1[i] != arr2[i]):
            return False
    return True


while(not isEqual(arr, start)):
    count += 1
    start[0] += 1
    start[1] += 1
    start[2] += 1
    if(start[0] != 15):
        start[0] = start[0] % 15
    if(start[1] != 28):
        start[1] = start[1] % 28
    if(start[2] != 19):
        start[2] = start[2] % 19

print(count)
