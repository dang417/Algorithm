import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    word = input()
    reversed_word =''.join(list(reversed(word)))
    reversed_word2 = word[::-1]
    print(f'#{tc} {reversed_word}')
    print(f'#{tc} {reversed_word2}')