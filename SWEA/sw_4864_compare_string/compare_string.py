import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t+1):
    str1 = input()
    str2 = input()
    if str1 in str2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')