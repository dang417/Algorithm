import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    case = input()
    stack = []

    for idx in range(len(case)):
        if case[idx] == '(':
            stack.append(case[idx])
    