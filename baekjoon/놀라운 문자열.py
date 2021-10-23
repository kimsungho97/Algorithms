#https://www.acmicpc.net/problem/1972

def show(line,issurprise):
    if issurprise:
        print(line+" is surprising.")
    else:
        print(line+" is NOT surprising.")

while True:
    line=input()
    if line=="*": 
        break
    else:
        n=len(line)
        issurprise=True
        if n==1:
            show(line,issurprise)
            continue
        else:
            for i in range(1,n):  #간격 수만큼 반복
                issurprise=True
                arr=[]
                for j in range(0,n-i):
                    arr.append(line[j]+line[j+i])
                tmp=set(arr)
                if len(tmp)!=len(arr):
                    issurprise=False
                    break
            show(line,issurprise)