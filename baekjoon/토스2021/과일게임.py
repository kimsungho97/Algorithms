def solution(fruitWeights, k):
    arr = sorted(fruitWeights, reverse=True)
    answer = sorted(list(set(arr[0:k])), reverse=True)
    return answer

print(solution([30,40,10,20,30],3))