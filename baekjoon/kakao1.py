def solution(s):
    word=['zero','one','two','three','four','five','six','seven','eight','nine']
    answer=s
    for i in word:
        answer=answer.replace(i,str(word.index(i)))
    answer=int(answer)
    return answer

print(solution("one4seveneight"))