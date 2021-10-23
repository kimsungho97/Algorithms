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


n1, n2 = list(map(int, input().split()))

a = max(n1, n2)
b = min(n1, n2)


gcd = GCD(a, b)
print(gcd)
print(int(a*b/gcd))
