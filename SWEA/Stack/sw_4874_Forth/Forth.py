import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t+1):
    forth = input().split()
    stack = []
    result = []
    try:
        for char in forth:
            rlt = 0
            if char in '*/-+':
                if char == '+':
                    rlt += int(stack.pop())
                    rlt = int(stack.pop()) + rlt
                    stack.append(int(rlt))

                elif char == '-':
                    rlt += int(stack.pop())
                    rlt = int(stack.pop()) - rlt
                    stack.append(int(rlt))

                elif char == '*':
                    rlt += int(stack.pop())
                    rlt = int(stack.pop()) * rlt
                    stack.append(int(rlt))

                elif char == '/':
                    rlt += int(stack.pop())
                    rlt = int(stack.pop()) // rlt
                    stack.append(int(rlt))

            elif char == '.':
                if len(stack) == 1:
                    result.append(stack[0])
            else:
                stack.append(char)
        if result:
            print(f'#{tc}', *result)

        else:
            print(f'#{tc} error')

    except:
        print(f'#{tc} error')