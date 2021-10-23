n, m = list(map(int, input().split()))

relations = {}
for i in range(m):
    a, b = list(map(int, input().split()))
    if(relations.get(a) == None):
        relations[a] = []
    if(relations.get(b) == None):
        relations[b] = []

    relations[a].append(b)
    relations[b].append(a)

result = False


def lookup(relations, path, current, visited):
    global result

    if(len(path) == 5):
        result = True
        return
    if(relations.get(current)==None):
        return
    for i in relations[current]:
        if(i == current or i in visited):
            continue
        lookup(relations, path+[i], i, visited+[i])


for i in range(n):
    lookup(relations, [i], i, [i])
    if(result):
        break

if(result):
    print(1)
else:
    print(0)
