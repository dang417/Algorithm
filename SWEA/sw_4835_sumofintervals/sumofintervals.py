import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))
    sum_list = []

    for i in range(n-m+1):
        sum_of_interval = 0
        for j in range(m):
            sum_of_interval += num_list[i+j]
        sum_list.append(sum_of_interval)

    for i in range(len(sum_list)):
        for j in range(len(sum_list)-1):
            if sum_list[j] > sum_list[j+1]:
                sum_list[j], sum_list[j+1] = sum_list[j+1], sum_list[j]

    print(f'#{tc+1} {sum_list[-1]-sum_list[0]}')
