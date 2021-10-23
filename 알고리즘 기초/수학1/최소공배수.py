# 유클리드 호제법
# GCD(A,B)=GCD(B,A%B)
# if A%B ==0
#   GCD=B
# else
#   GCD(B,A%B)

def GCD(A, B):
    if(A % B == 0):
        return B
    else:
        return GCD(B, A % B)


n = int(input())

for _ in range(n):
    n1, n2 = list(map(int, input().split()))
    a, b = max(n1, n2), min(n1, n2)
    print(int(a*b/GCD(a, b)))
