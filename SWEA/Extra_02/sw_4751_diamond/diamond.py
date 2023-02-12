import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t+1):
    word = input()
    print('..#.' * len(word), end = '.')
    print()
    print('.#' * 2 * len(word), end = '.')
    print()
    for i in word:
        print(f'#.{i}.', end = '')
    print('#')
    print('.#' * 2 * len(word), end='.')
    print()
    print('..#.' * len(word), end='.')
    print()