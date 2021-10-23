n,line=list(map(int,input().split()))

line=list(str(line))

texts=[''' -- 
|  |
|  |
    
|  |
|  |
 -- ''',
'''    
   |
   |
    
   |
   |
    ''',
'''
 -- 
   |
   |
 -- 
|   
|   
 -- ''',
  ''' -- 
   |
   |
 -- 
   |
   |
 -- ''',
 '''
|  |
|  |
 -- 
   |
   |
    ''',
''' -- 
|   
|   
 -- 
   |
   |
 -- ''',
 ''' -- 
|   
|   
 -- 
|  |
|  |
 -- ''',
 ''' -- 
   |
   |
    
   |
   |
    ''',
   ''' -- 
|  |
|  |
 -- 
|  |
|  |
 -- ''',
 ''' -- 
|  |
|  |
 -- 
   |
   |
 -- '''
 ]
for i in range(7):
    for j in line:
        if(int(j)==4):
            if(i==0):
                print(' '*4,end=' ')
            else:
                print(texts[int(j)][(i-1)*5:(i-1)*5+5].strip('\n'),end=' ')
        else:
            print(texts[int(j)][i*5:i*5+5].strip('\n'),end=' ')
    print()