#n- 숫자 갯수 / arr- 숫자 / selected- 고른 숫자 / cur_index- 마지막까지 고른 숫자 인덱스
def print_lotto(n, arr, selected, cur_index):
    #6개의 숫자가 모두 골라졌을 경우 출력
    if len(selected)==6:
        print(' '.join(list(map(str,selected))))
    else:
        for index in range(cur_index,n):
            #길이가 6개인 번호 조합을 완성시키지 못한다면 종료
            if (n-cur_index)+len(selected)<6:
                break
            #재귀
            print_lotto(n,arr,selected+[arr[index]],index+1)


while True:
    # 숫자들을 입력받음
    arr=list(map(int,input().split()))
    # 숫자들의 갯수
    n=arr[0]
    #0을 입력받았을 경우 종료
    if n==0:
        break
    del arr[0]

    print_lotto(n,arr,[],0)
    #줄바꿈
    print()





