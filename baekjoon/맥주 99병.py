#https://www.acmicpc.net/problem/17293

K=int(input())

for i in range(K,-1,-1):
    if(i>1):
        print(f'{i} bottles of beer on the wall, {i} bottles of beer.')
        if(i==2):
            print(f'Take one down and pass it around, {i-1} bottle of beer on the wall.')
        else:
            print(f'Take one down and pass it around, {i-1} bottles of beer on the wall.')
        print()
    elif(i==1):
        print(f'{i} bottle of beer on the wall, {i} bottle of beer.')
        print(f'Take one down and pass it around, no more bottles of beer on the wall.')
        print()
    elif(i==0):
        print('No more bottles of beer on the wall, no more bottles of beer.')
        if K==1:
            print(f'Go to the store and buy some more, {K} bottle of beer on the wall.')    
        else:
            print(f'Go to the store and buy some more, {K} bottles of beer on the wall.')
