import sys
lines = sys.stdin.readlines()

for line in lines:

    small, big, num, space = 0, 0, 0, 0
    for i in line:
        if(ord(i) >= ord('a') and ord(i) <= ord('z')):
            small += 1
        elif(ord(i) >= ord('A') and ord(i) <= ord('Z')):
            big += 1
        elif(i.isdigit()):
            num += 1
        elif(i == ' '):
            space += 1
    print(small, big, num, space)
