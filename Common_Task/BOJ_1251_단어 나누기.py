word = input()
n = len(word)
min_ord = 0

for i in range(n-2):
    if ord(word[min_ord]) > ord(word[i]):
        min_ord = i

sec_min = min_ord+1
for i in range(min_ord+1, n-1):
    if ord(word[sec_min]) > ord(word[i]):
        sec_min = i

left = word[:min_ord+1]
middle = word[min_ord+1:sec_min+1]
right = word[sec_min+1:]

rlt = left[::-1] + middle[::-1] + right[::-1]

print(rlt)




    