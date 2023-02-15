import sys
sys.stdin = open('input.txt')

n = int(input())
meet_list = [0] * n

for i in range(n):
    meet_list[i] = list(map(int,input().split()))

meet_list.sort(key = lambda x : (x[0], x[1]))

cnt = 1
pre_meet = meet_list[0]

for i in range(1,n):
    if pre_meet[1] <= meet_list[i][0]:
        pre_meet = meet_list[i]
        cnt += 1

print(cnt)