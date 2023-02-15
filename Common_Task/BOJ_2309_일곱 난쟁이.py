height_list = []
for i in range(9):
    height_list.append(int(input()))

height_list.sort()

for i in height_list:
    for j in height_list:
        if sum(height_list) - i - j == 100 and i != j:
            height_list.remove(i)
            height_list.remove(j)
            break
        
for i in height_list:
    print(i)