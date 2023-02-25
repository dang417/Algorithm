# 남학생은 자기가 받은 수의 배수이면 그 스위치 상태를 바꾼다
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 대칭이면서
# 가장 많은 스위치를 포함하는 구간을 찾아서 바꾼다

import sys
sys.stdin = open('input.txt')

n = int(input())
switch = list(map(int, input().split()))
m = int(input())
for i in range(m):
    gender, num = map(int, input().split())
    if gender == 1:
        for j in range(n):
            if (j+1) % num == 0:
                if switch[j]:
                    switch[j] = 0
                else:
                    switch[j] = 1
    else:
        left, right = 0, 0
        j = num - 1
        while True:
            if j - left < 0 or j + right == n:
                break
            if switch[j - left] == switch[j + right]:
                if switch[j - left]:
                    switch[j - left], switch[j + right] = 0, 0
                else:
                    switch[j - left], switch[j + right] = 1, 1
                left += 1
                right += 1
            else:
                break
if n > 20:
    for i in range(0, n, 20):
        j = i + 20
        print(*switch[i : j])
else:
    print(*switch)