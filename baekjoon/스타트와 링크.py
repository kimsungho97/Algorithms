n=int(input())
arr=[]

for i in range(n):
    temp=list(map(int,input().split()))
    arr.append(temp.copy())

#최소값을 저장할 변수
result=100



#점수 계산해주는 함수
def calc_score(team,arr,score,cur_index):
    if cur_index==len(team):
        return score
    else:
        for i in range(len(team)):
            score+=arr[team[cur_index]][team[i]]
        return calc_score(team,arr,score,cur_index+1)
        

#arr: 모든 선수들
#team: 한쪽 팀에 편성된 선수들
#n: 총 인원수
def brute_force(arr, team, n):
    global result

    #한쪽 팀이 완성되었을 때
    if len(team)==int(n/2):
        score1=0
        score2=0
        team2=[i for i in range(n)]
        for i in team:
            team2.remove(i)
        #팀 점수계산
        score1=calc_score(team,arr,0,0)
        score2=calc_score(team2,arr,0,0)
        result_temp=abs(score1-score2)
        if result > result_temp:
            result= result_temp
    elif len(team)==0:
        for i in range(int(n/2)):
            brute_force(arr, [i], n)
    else:
        for i in range(team[-1]+1,n):
            brute_force(arr,team+[i],n)
        


brute_force(arr,[],n)

print(result)