#https://www.acmicpc.net/problem/15998

n = int(input())

money = 0
expect_before = 0
for i in range(n):
    [a, b] = list(map(int, input().split()))

    if a < 0 and money < abs(a):
        if expect_before == 0:
           expect_before = b-a-money
        else:
            if expect_before < (b-a-money):
                if (b-a-money) % expect_before != 0:
                    expect_before = -1
                    break
            else:
                if expect_before % (b-a-money) != 0:
                    expect_before = -1
                    break
                else:
                    expect_before = b-a-money
            if expect_before<b:
                expect_before=-1
                break
    elif a > 0:
        if b != a+money:
            expect_before = -1
            break
    elif a < 0:
        if a+money != b:
            expect_before = -1
            break
    
    money = b

if(expect_before==0):
    print(1)
else:
    print(expect_before)
