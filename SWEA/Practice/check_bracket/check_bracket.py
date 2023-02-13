# stack = [0] * 3

# top = -1
#
# top += 1 # push(10)
# stack[top] = 10
# print(stack)
#
# top += 1 # push(20)
# stack[top] = 20
# print(stack)
#
# top += 1 # push(30)
# stack[top] = 30
# print(stack)
#
# top -= 1
# print(stack[top+1])
#
# top -= 1
# print(stack[top+1])
#
# top -= 1
# print(stack[top+1])

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    bracket = input()
    stack = []
    result = 1
    for char in bracket:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                result = -1
                break
    else:
        if stack:
            result = -1

    print(result)

