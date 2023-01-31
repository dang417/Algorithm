n = input()
num = []
for char in n:
    num.append(char)

num = sorted(num,reverse = True)
for i in num:
    print(int(i),end='')