import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in  range(1, t+1):
    cal = input()
    stack = []
    result = 0

    for char in cal:
        if char not in '+-*/':
            stack.append(char)
        else:
            x = int(stack.pop())
            y = int(stack.pop())
            if char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)
            elif char == '*':
                stack.append(y * x)
            elif char == '/':
                stack.append(y / x)
    result = stack.pop()
    print(result)