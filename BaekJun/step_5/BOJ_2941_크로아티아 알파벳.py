word = input()
cro_dict = {
    1 : 'c=',
    2 : 'c-',
    3 : 'dz=',
    4 : 'd-',
    5 : 'lj',
    6 : 'nj',
    7 : 's=',
    8 : 'z=',
}

count = 0

for i in range(1,9):
    if cro_dict[i] in word:
        count += word.count(cro_dict[i])

print(len(word)-count)