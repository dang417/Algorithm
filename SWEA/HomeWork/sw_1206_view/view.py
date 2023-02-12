import sys
sys.stdin = open('input.txt')

for t in range(10):
    n = int(input())
    height_list = list(map(int, input().split()))
    rlt = 0
    for i in range(2, n-2):
        for buil in height_list[i-2:i]+height_list[i+1:i+3]:
            if buil >= height_list[i]:
                break
        else:
            tmp_list = height_list[i-2:i+3]
            for j in range(5):
                for k in range(4):
                    if tmp_list[k] > tmp_list[k+1]:
                        tmp_list[k], tmp_list[k+1] = tmp_list[k+1], tmp_list[k]
            rlt += tmp_list[-1] - tmp_list[-2]
    
    print(f'#{t+1} {rlt}')