import sys


n = int(input())
queue = []
for i in range(n):
    cmd = sys.stdin.readline().strip()
    num = 0
    if(len(cmd.split(' ')) != 1):
        cmd, num = cmd.split(' ')
        num = int(num)

    if(cmd == 'push'):
        queue.append(num)
    elif(cmd == 'back'):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[-1])
    elif(cmd == 'front'):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[0])
    elif(cmd == 'size'):
        print(len(queue))
    elif(cmd == 'pop'):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[0])
            del queue[0]
    elif(cmd == 'empty'):
        if(len(queue) == 0):
            print(1)
        else:
            print(0)
