import sys
sys.stdin = open('sample_input.txt')
input = sys.stdin.readline

# '00 0111011 0110001 0111011 0110001 0110001 0001101 0010011 0111011 00'
# '00 0111011 0110001 0111011 0110001 0110001 0001101 0010011 0111011 00'
# '0111011 0110001 0111011 0110001 0110001 0001101 0010011 0111011'
# '0 0011001 0110111 0101111 0001011 0100011 0001011 0110001 0101111'
# '0011001 0100011 0100011 0101111 0110111 0010011 0010011 0111011'

# 이진수로 변환한 후에 뒤쪽 1에서부터 7자리씩 끊으면서 입력 받아야 함
#

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    for i in range(n):
        code = input().rstrip()
        print(code)