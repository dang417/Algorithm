import sys
sys.stdin = open('input.txt')

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

for tc in range(1, 11):
    n = int(input())
    mtx_row = [''] * 8
    mtx_col = [''] * 8
    cnt = 0

    for _ in range(8):
        row = input()
        mtx_row[_] = row

    for i in range(8):
        for j in range(8):
            mtx_col[i] += mtx_row[j][i]

    # 가로 검사
    for rows in mtx_row:
        for i in range(8-n+1):
            if isPalindrome(rows[i:i+n]):
                cnt += 1

    # 세로 검사
    for cols in mtx_col:
        for i in range(8-n+1):
            if isPalindrome(cols[i:i+n]):
                cnt += 1

    print(f'#{tc}', cnt)

