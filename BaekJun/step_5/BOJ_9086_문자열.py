import sys
sys.stdin = open('input.txt')

t = int(input())
for _ in range(t):
    word = input()
    print(word[0]+word[-1])