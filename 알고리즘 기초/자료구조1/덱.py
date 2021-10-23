import sys
n = int(input())
deck = []
size = 0

for i in range(n):
    cmd = sys.stdin.readline().strip()
    num = None
    if(len(cmd.split()) == 2):
        cmd, num = cmd.split()

    if(cmd == "push_back"):
        deck.append(int(num))
        size += 1

    elif(cmd == "push_front"):
        deck = [int(num)]+deck
        size += 1

    elif(cmd == "front"):
        if(size == 0):
            print(-1)
        else:
            print(deck[0])
    elif(cmd == "back"):
        if(size == 0):
            print(-1)
        else:
            print(deck[-1])
    elif(cmd == "empty"):
        if(size == 0):
            print(1)
        else:
            print(0)
    elif(cmd == "pop_front"):
        if(size == 0):
            print(-1)
        else:
            print(deck[0])
            deck = deck[1:]
            size -= 1
    elif(cmd == "pop_back"):
        if(size == 0):
            print(-1)
        else:
            print(deck.pop())
            size -= 1
    elif(cmd == "size"):
        print(size)
