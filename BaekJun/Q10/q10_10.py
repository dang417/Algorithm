n = int(input())

words_list = []

for i in range(n):
    words_list.append(input())

words_list = list(set(words_list))

words_list.sort(key = lambda x : (len(x), x))

for j in range(len(words_list)):
    print(words_list[j])