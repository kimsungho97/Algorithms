

def solution(places):
    answer = []
    for _ in range(len(places)):
        place=places[_]

        is_safe=1
        human=[]
        for i in range(len(place)):
            place[i]=list(place[i])
        #사람 위치 저장
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j]=='P':
                    human.append((i,j))
        for i in human:
            for j in human:
                if i==j:
                    continue
                else:
                    #거리가 2 초과인 경우
                    if abs(j[0]-i[0])>2 or abs(abs(j[1]-i[1])>2):
                        continue
                    elif (abs(j[0]-i[0])==2 and abs(abs(j[1]-i[1])>0)) or (abs(j[0]-i[0])>0 and abs(abs(j[1]-i[1])==2)) :
                        continue
                    #그렇지 않은경우(칸막이 확인)
                    else:
                        #같은 행/열에 존재하는 경우
                        if j[0]==i[0] or j[1]==i[1]:
                            if abs(j[0]-i[0])==1 or abs(j[1]-i[1])==1:
                                is_safe=0
                                break
                            #거리가 2일때
                            elif (abs(j[0]-i[0])==2 or abs(j[1]-i[1])==2) and place[int((i[0]+j[0])/2)][int((i[1]+j[1])/2)]!='X':
                                is_safe=0
                                break
                        #대각선위치
                        elif abs(j[0]-i[0])==1 and abs(j[1]-i[1])==1:
                            if not(place[i[0]][j[1]]=='X' and place[j[0]][i[1]]):
                                is_safe=0
                                break
        answer.append(is_safe)
                            
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))