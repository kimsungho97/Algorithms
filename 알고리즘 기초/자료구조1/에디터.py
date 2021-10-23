st1 = list(input())
st2 = []
n = int(input())

cmd = []
for i in range(n):
    cmd.append(input())

for i in cmd:
    if i[0] == 'L' and len(st1) != 0:
        st2.append(st1.pop())
    elif i[0] == 'D' and len(st2) != 0:
        st1.append(st2.pop())
    elif i[0] == 'B' and len(st1) != 0:
        st1.pop()
    elif i[0] == 'P':
        st1.append(i[2])

while len(st2) != 0:
    st1.append(st2.pop())

print("".join(st1))
