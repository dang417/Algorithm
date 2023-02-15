import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    cal = input()
    stack = [] # 연산자들을 담아둘 stack
    result = '' # 최종 결과값
    # 전체 식 순회
    for char in cal:
        # 연산자 들이라면
        if char in '+-*/()':
            # print(char)
            # 연산자들의 우선순위에 맞춰서 값들을 stack에 넣는 과정
            if char == '(':
                stack.append(char)
            elif char in '*/':
                while stack and stack[-1] != '(' and stack[-1] not in '+-':
                    result += stack.pop()
                stack.append(char)
            elif char in '+-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
        else:
            result += char
    while stack:
        result += stack.pop()
    print(result)