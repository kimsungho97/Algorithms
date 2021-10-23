def solution(orderAmount, taxFreeAmount, serviceFee):
    # orderAmount : 주문금액
    # taxFreeAmount : 비과세금액
    # serviceFee : 봉사료
    answer=0
    import math
    taxAmount = orderAmount - taxFreeAmount - serviceFee
    if taxAmount == 1:
        answer = 0
    else:
        answer = taxAmount / 11.0
        if (int(answer) != answer):
            answer = int(answer) + 1
        
    return answer