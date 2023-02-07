import sys
sys.stdin = open('input.txt')
# 오 아 왼 위 를 돌아가며
# array의 값이 0이 아닐때마다
# num_list의 다음 값을 +=


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = []
    print(arr)
    num_list = list(range(1, n+1))
    print(num_list)

    for i in range(n):
        row = [0] * n
        arr.append(row)

    i = 0
    j = 0
    k = 0

    while num_list != []:
        while arr[i][j+1] == 0:
            arr[i][j] += num_list[k]
            num_list.remove(num_list[k])
            j += 1

        while arr[i+1][j] == 0:
            arr[i][j] += num_list[k]
            num_list.remove(num_list[k])
            i += 1

        while arr[i][j-1] == 0:
            arr[i][j] += num_list[k]
            num_list.remove(num_list[k])
            j -= 1

        while arr[i-1][j] == 0:
            arr[i][j] += num_list[k]
            num_list.remove(num_list[k])
            i -= 1

    print(arr)





