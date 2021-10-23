#https://www.acmicpc.net/problem/1439
line=input()
new_line=str()
groups=[]
last_char=None
for i in range(len(line)):
    if last_char==None:
        last_char=line[i]
    elif last_char==line[i]:
        continue
    elif last_char!=line[i]:
        last_char=line[i]
    new_line+=last_char


count1=0
count0=0
for i in range(len(new_line)):
    if(new_line[i]=='1'):
        count1+=1
    else:
        count0+=1

print(min(count0,count1))
