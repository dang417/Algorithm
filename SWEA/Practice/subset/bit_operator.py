arr = ['a', 'b', 'c', 'd']
N = len(arr)

# arr에 대한 모든 경우의 수
for i in range(1 << N):
    # arr의 idx
    for j in range(N):
        print('='*30)
        # i : 모든 경우의 수 중, i번째
        # j : 부분집합에 포함될 arr의 j번째
        # 1<<j : arr의 j번째 요소의 비트
        print(f'i : {i} | j : {j} | 1<<j : {1<<j}')
        # i == 0 : 0번째 경우의 수 비트 : [0, 0, 0, 0] == 공집합
        # i == 1 : 1번째 경우의 수 비트 : [0, 0, 0, 1]
        # 2진수로 바꿔보자면
        print(f'{bin(i)[2:]:0>4}  {bin(1<<j)[2:]:0>4}')
        # i의 j번 비트가 1인 경우
        # i == 5 : [0, 1, 0, 1]
        # 1 << 0 : [0, 0, 0, 1] True
        # 1 << 1 : [0, 0, 1, 0] False
        # 1 << 2 : [0, 1, 0, 0] True
        # 1 << 3 : [1, 0, 0, 0] False
        print(f'{i & 1<<j} : {bin(i & 1<<j)[2:]:0>4}')
        if i & (1<<j):
            print(f'{j}번 째 요소 == {arr[j]}')
            # print(arr[j], end=' ')
        print('='*30)
        print()
    print()