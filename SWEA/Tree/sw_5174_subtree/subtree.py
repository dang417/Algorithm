import sys
sys.stdin = open('sample_input.txt')

def inorder(node):
    global k
    if node != 0:
        inorder(left[node])
        k += 1
        inorder(right[node])

t = int(input())

for tc in range(1, t+1):
    e, n = map(int, input().split())
    pc = list(map(int, input().split()))
    parent = [0] * (e+2)
    left = [0] * (e+2)
    right = [0] * (e+2)
    k = 0
    for i in range(0, len(pc)-1, 2):
        parent[pc[i+1]] = pc[i]
        if left[pc[i]] == 0:
            left[pc[i]] = pc[i+1]
        else:
            right[pc[i]] = pc[i+1]
    inorder(n)

    print(f'#{tc}', k)