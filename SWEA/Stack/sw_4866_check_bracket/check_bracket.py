import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for tc in range(1, t+1):

    word = input()
    result = 1
    stack = []

    for char in word:
        if char == '(' or char == '{':
            stack.append(char)
        else:
            if char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                elif not stack:
                    result = 0
                    break
                elif stack[-1] != '(':
                    result = 0
                    break
            if char == '}':
                if not stack or stack[-1] != '{':
                    result = 0
                    break
                else:
                    stack.pop()
    if stack:
        result = 0
    print(f'#{tc}', result)