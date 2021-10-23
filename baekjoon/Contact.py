# https://www.acmicpc.net/problem/1013


n = int(input())
testcases = []
answer = []
for i in range(n):
    testcases.append(input())

for line in testcases:
    temp = ''
    chk100 = False
    chk1 = False
    prev = False
    chk_wrong = False
    for c in line:
        #print(temp, "<-", c)
        if chk100 and (not chk1):
            if c == '0':
                continue
            elif c == '1':
                chk1 = True
                continue
        elif chk1:
            if c == '1':
                temp = c
                prev = True
                continue
            elif c == '0':
                chk100 = False
                chk1 = False
                temp += c
                continue
        else:
            temp = temp+c

        if temp == '100' or (prev and temp == '1100'):
            temp = ''
            chk100 = True
            prev = False
            continue
        elif temp == '01' or (prev and temp == '101'):
            temp = ''
            prev = False
            continue
    # print(temp)
    if chk100 != chk1:
        answer.append(False)
    elif len(temp) != 0 and temp != '1':
        answer.append(False)
    elif temp == '1' and not prev:
        answer.append(False)
    else:
        answer.append(True)

for i in answer:
    if i:
        print("YES")
    else:
        print("NO")
