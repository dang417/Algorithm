t = int(input())
group_words = []
for i in range(1,t+1):
    word = input()
    if len(word) == 1:
        group_words.append(word)
        continue
    if len(word) == 0:
        continue
    for j in range(len(word)-1):
        if word[j] != word[j+1] and word[j] in word[j+1:]:
            break
    else : 
        group_words.append(word)

print(len(group_words))