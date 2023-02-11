import sys
sys.stdin = open('sample_input.txt')

def isPalindrome(str):
    a = len(str)
    reversed_str = ''

    for i in range(len(str)-1, -1, -1):
        reversed_str += str[i]

    if a % 2 == 0:
        if reversed_str[:a//2] == str[:a//2]:
            return True
        else:
            return False
    else:
        if reversed_str[:(a // 2)+1] == str[:(a // 2)+1]:
            return True
        else:
            return False


t = int(input())

for tc in range(1, t+1):
    n, m = map(int,input().split())
    mtx_row = [''] * n
    mtx_col = [''] * n

    for _ in range(n):
        row = input()
        mtx_row[_] = row

    for i in range(n):
        for j in range(n):
            mtx_col[i] += mtx_row[j][i]

    # 가로 검사
    for rows in mtx_row:
        for i in range(n-m+1):
            if isPalindrome(rows[i:i+m]):
                print(f'#{tc}', rows[i:i+m])
                break

    # 세로 검사
    for cols in mtx_col:
        for i in range(n-m+1):
            if isPalindrome(cols[i:i+m]):
                print(f'#{tc}', cols[i:i+m])
                break






