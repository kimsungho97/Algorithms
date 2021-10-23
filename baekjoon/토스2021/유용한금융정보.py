def solution(input):
    arr=input.split("\n")
    m, n = list(map(int, arr[0].split(" ")))
    answer = arr[0]+"\n"
    showcount=0
    daycount=0
    for cmd in arr[1:]:
        if cmd == 'SHOW':
            if showcount >= n:
                answer+="0"
            else:
                answer += "1"
                showcount += 1
                
        elif cmd == 'NEGATIVE':
            answer+="0"
            showcount=n

        elif cmd == 'NEXT':
            if showcount == n:
                daycount += 1
                if daycount > m:
                    daycount=0
                    showcount = 0
            answer+="-"
        elif cmd == 'EXIT':
            answer += "BYE"
            return answer
        else:
            answer+="ERROR"

        answer += "\n"
        
