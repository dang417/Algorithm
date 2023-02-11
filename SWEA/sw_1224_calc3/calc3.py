import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    operation = input()

    for s in operation:
        if