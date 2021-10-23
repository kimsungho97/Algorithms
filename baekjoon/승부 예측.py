#https://www.acmicpc.net/problem/15997

teams=input().split(' ')

team_n=len(teams)
n=int(team_n*(team_n-1)/2)

teams_wins=dict()
for i in teams:
    teams_wins[i]=0

for i in range(0,n):
    line=input().split(" ")
    [a,b]=line[:2]
    a_win=float(line[2])
    b_win=float(line[4])
    if(a_win+b_win!=1):
        total=a_win+b_win
        a_win=a_win/total
        b_win=b_win/total

    teams_wins[a]+=a_win
    teams_wins[b]+=b_win

total=sum(list(teams_wins.values()))/2
for i in teams:
    teams_wins[i]/=total
    print("{:.10f}".format(teams_wins[i]))
