import sys
sys.stdin = open('input.txt')

word_list = []
word = ''
while True:
    word = input()
    if word == '.':
        break
    word_list.append(word)

for word in word_list:
    stack = []
    for char in word:
        if char == '(' or char == '[':
            stack.append(char)
        try:
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == ')' or char == ']':
                print('no')
                break
        except:
            print('no')
            break

    else:
        if stack:
            print('no')
        else:
            print('yes')