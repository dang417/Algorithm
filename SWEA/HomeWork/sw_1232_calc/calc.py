import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    tree = [0] * (n + 1)
    for i in range(n):
        a = list(input().split())
        tree[int(a[0])] = a[1]
        if len(a) == 4:
            left[int(a[0])] = int(a[2])
            right[int(a[0])] = int(a[3])
    for i in range(n, 0, -1):
        if tree[i] in '+-*/':
            if tree[i] == '+':
                tree[i] = int(tree[left[i]]) + int(tree[right[i]])
            elif tree[i] == '-':
                tree[i] = int(tree[left[i]]) - int(tree[right[i]])
            elif tree[i] == '*':
                tree[i] = int(tree[left[i]]) * int(tree[right[i]])
            elif tree[i] == '/':
                tree[i] = int(tree[left[i]]) // int(tree[right[i]])
    print(f'#{tc}', tree[1])
