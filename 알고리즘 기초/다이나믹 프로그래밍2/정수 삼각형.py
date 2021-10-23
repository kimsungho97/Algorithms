import sys

n = int(input())
tree = []

for _ in range(n):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(n-2, -1, -1):
    for j in range(len(tree[i])):
        tree[i][j] += max(tree[i+1][j], tree[i+1][j+1])

print(tree[0][0])
