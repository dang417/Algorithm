import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t+1):
    str_case = input()
    n = len(str_case)

    while True:
        for i in range(n-2):
            if str_case[i] == str_case[i+1]:
                str_case = str_case[:i] + str_case[i+2:]
                n -= 2
                break
        else:
            break
    if str_case[-1] == str_case[-2]:
        str_case = str_case[:-2]

    print(f'#{tc}', len(str_case))

# for tc in range(1, t+1):
#     word = input()
#     stack = []
#
#     for char in word:
#
#         if stack and stack[-1] == char:
#             stack.pop()
#         else:
#             stack.append(char)
#
#     print(stack)