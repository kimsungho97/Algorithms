def solution(servers, sticky, requests):
    answer = [[] for _ in range(servers)]
    memory = {}
    cur=0
    if(sticky):
        for i in requests:
            if (memory.get(i) != None):
                answer[memory[i]].append(i)
            else:
                answer[cur%servers].append(i)
                memory[i]=cur
                cur+=1
    else:
        for i in requests:
            answer[cur % servers].append(i)
            cur += 1
            
    return answer