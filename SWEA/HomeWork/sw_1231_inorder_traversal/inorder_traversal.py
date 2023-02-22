import sys
sys.stdin = open('input.txt')

def inorder(node):
    global k
    if node != 0:
        inorder(left[node])
        print(word[node], end = '')
        inorder(right[node])

for tc in range(1, 11):
    n = int(input())
    left = [0] * (n+1)
    right = [0] * (n+1)
    word = {}
    for i in range(n):
        a = list(input().split())
        word[int(a[0])] = a[1]
        if len(a) >= 3:
            left[int(a[0])] = int(a[2])
        if len(a) == 4:
            right[int(a[0])] = int(a[3])
    print(f'#{tc}', end=' ')
    inorder(1)
    print()