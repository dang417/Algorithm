word = input()
n = len(word)
word_list = []

for i in range(1, n-1):
    for j in range(i+1, n):
        left = word[:i]
        middle = word[i:j]
        right = word[j:]
        changed = left[::-1] + middle[::-1] + right[::-1]
        word_list.append(changed)

print(sorted(word_list)[0])
