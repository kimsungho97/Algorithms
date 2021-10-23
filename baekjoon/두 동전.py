import copy

row, col= list(map(int,input().split()))
origin_board=[]

for i in range(row):
    line=list(input())
    origin_board.append(line)


token={'coin': 'o', 'empty':'.', 'wall':'#'}

moving=['up','down','left','right']

count=11

def coin_move(before,direction):
    global row, col, token
    drop_count=0
    
    board=before[:]

    if direction=='up':
        for r in range(row):
            for c in range(col):
                if board[r][c]==token['coin']:
                    if r==0:
                        board[r][c]=token['empty']
                        drop_count+=1
                    elif board[r-1][c]==token['empty']:
                        board[r][c]=token['empty']
                        board[r-1][c]=token['coin']
                    elif board[r-1][c]==token['coin']:
                        return (-1,board)
    if direction=='down':
        for r in range(row-1,-1,-1):
            
            for c in range(col):
                if board[r][c]==token['coin']:
                    if r==row-1:
                        board[r][c]=token['empty']
                        drop_count+=1
                    elif board[r+1][c]==token['empty']:
                        board[r][c]=token['empty']
                        board[r+1][c]=token['coin']
                    elif board[r+1][c]==token['coin']:
                        return (-1,board)
    if direction=='left':
        for r in range(row):
            for c in range(col):
                if board[r][c]==token['coin']:
                    if c==0:
                        board[r][c]=token['empty']
                        drop_count+=1
                    elif board[r][c-1]==token['empty']:
                        board[r][c]=token['empty']
                        board[r][c-1]=token['coin']
                    elif board[r][c-1]==token['coin']:
                        return (-1,board)
    if direction=='right':
        for r in range(row):
            for c in range(col-1,-1,-1):
                if board[r][c]==token['coin']:
                    if c==col-1:
                        board[r][c]=token['empty']
                        drop_count+=1
                    elif board[r][c+1]==token['empty']:
                        board[r][c]=token['empty']
                        board[r][c+1]=token['coin']
                    elif board[r][c+1]==token['coin']:
                        return (-1,board)
    return (drop_count,board)

def is_eqaul(before,after):
    global row, col
    coin_count=0
    for r in range(row):
        for c in range(col):
            temp=before[r][c]
            if(temp==token['wall']):
                continue
            if temp!=after[r][c]:
                return False
            if temp==token['coin']:
                coin_count+=1
            if coin_count==2:
                return True
    return True

def move(original,before, cur_count):
    global row, col, token, count, moving

    
    for m in moving:
        
        drop_count, after=coin_move(copy.deepcopy(before),m)
        #print(cur_count)
        if cur_count>=11:
            break
        if drop_count==1 and cur_count<count:
            count=cur_count
            break
        if drop_count==-1 or drop_count==2:
            continue
        if is_eqaul(before,after):
            continue

        move(original, after, cur_count+1)

move(origin_board,copy.deepcopy(origin_board),1)
            
if count>=11:
    print(-1)
else:
    print(count)
