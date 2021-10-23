line=input()

while(len(line)>=10):
    print(line[:10])
    line=line[10:]

print(line)