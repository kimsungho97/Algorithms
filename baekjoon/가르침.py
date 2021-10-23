import copy

def alpha_to_index(alpha):
    return ord(alpha)-ord('a')
    


n, k =list(map(int,input().split()))
words=[]

for i in range(n):
    words.append(input())

alpha_count=[0 for i in range(26)]
alpha_count[alpha_to_index('a')]=1
alpha_count[alpha_to_index('n')]=1
alpha_count[alpha_to_index('t')]=1
alpha_count[alpha_to_index('i')]=1
alpha_count[alpha_to_index('c')]=1


each_words_count=[]

for i in range(n):
    each_words_count.append(copy.deepcopy(alpha_count))

for i in range(n):
    word=words[i]
    for j in word:
        each_words_count[i][alpha_to_index(j)]=1

all_alpha=copy.deepcopy(alpha_count)
longest_word=0
for i in range(n):
    for j in range(26):
        if each_words_count[i][j]==1:
            all_alpha[j]=1
    


max_count=0
total=sum(all_alpha)

def brute_force(k, each_words, all_alpha, pick_alpha, cur_index):
    global max_count

    if(sum(pick_alpha)==min(total,k)):
        count=0
        for word in each_words:
            temp=[0 for i in range(26)]
            for i in range(26):
                temp[i]=pick_alpha[i]-word[i]
            if not -1 in temp:
                count+=1
        
        if max_count<count:
            max_count=count
        
    else:
        for i in range(cur_index,26):
            if(pick_alpha[i]!=1 and all_alpha[i]==1):
                pick_alpha[i]=1
                brute_force(k, each_words, all_alpha, pick_alpha, i)
                pick_alpha[i]=0
    

brute_force(k,each_words_count,all_alpha,alpha_count, 0)

print(max_count)

