word = input().lower() #lower 함수로 입력을 소문자로만 받는다
word_list = list(set(word))
result = []
char_list = []
for char in word:
    char_list.append(char)
for char in word_list:
    result.append(word.count(char))

if result.count(max(result)) >= 2:
    print('?')
else :
    print(word_list[result.index(max(result))].upper())