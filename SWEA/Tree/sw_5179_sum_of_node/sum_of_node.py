# 완전 이진 트리
# 리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합
# 리프노드에 저장된 값은 주어짐 (부모 노드 == 자식 노드 두개의 합)
# 노드 번호는 루트가 1 왼쪽에서 오른쪽으로 증가 (BFS)
# 지정한 노드 번호에 저장된 값을 출력하는 프로그램 작성

import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n, m, l = map(int, input().split())
    tree = [0] * (n+1)
    for i in range(m):
        no, num = map(int, input().split())
        tree[no] = num
    if n % 2 == 0:
        tree[n//2] = tree[-1]
        for i in range(n-m-1, 0, -1):
            tree[i] = tree[(i*2)] + tree[(i*2)+1]
    else:
        for i in range(n-m, 0, -1):
            tree[i] = tree[i*2] + tree[(i*2)+1]
    print(f'#{tc}', tree[l])