n = int(input())

length = 0
k = 1
each = 10

while(n >= each):
    length += (each-int(each/10))*k

    k += 1
    each *= 10

each = int(each/10)
#print((n-each+1), k)
length += (n-each+1)*k


print(length)
