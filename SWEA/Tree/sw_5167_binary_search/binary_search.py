import sys
sys.stdin = open('sample_input.txt')

def inorder(node):
    global k
    if node != 0:
        inorder(left[node])
        tree[node] = k
        k += 1
        inorder(right[node])

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    parent = [0] * (n+1)
    left = [0] * (n+1)
    right = [0] * (n+1)

    for i in range(n+1):
        parent[i] = i//2
        if n % 2 == 0:
            if 0 < i <= n//2:
                left[i] = i * 2
            if 0 < i <= (n//2) - 1:
                right[i] = (i * 2) + 1
        else:
            if 0 < i <= n//2:
                left[i] = i * 2
            if 0 < i <= n//2:
                right[i] = (i * 2) + 1

    tree = [0] * (n+1)
    k = 1
    for i in range(n+1):
        if i != 0 and parent[i] == 0:
            root = i

    inorder(root)
    print(f'#{tc}', tree[1], tree[n//2])