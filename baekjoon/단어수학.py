n=int(input())
words=[]
for i in range(n):
    words.append(input())


#가장 긴 문자열의 길이 파악
max_len=max(map(lambda x:len(x),words))


#우선순위를 숫자 크기로로 저장(빈도*(10^자리수))
priority={}
for word in words:
    for i in range(len(word)):
        # 자리수 + 빈도
        if(priority.get(word[i])==None):
            priority[word[i]]=0
        priority[word[i]]+=10**(len(word)-i-1)

#우선순위 가장 큰 알파벳부터 숫자 배정
priority=sorted(list(priority.items()),key=lambda x:x[1],reverse=True)
alpha={}
nums=[i for i in range(0,10)]
for key,value in priority:
    alpha[key]=nums.pop()

    
result=0
for word in words:
    word_to_num=0
    for i in range(len(word)):
        word_to_num+=(10**(len(word)-i-1) * alpha[word[i]])
    result+=word_to_num

print(result)

