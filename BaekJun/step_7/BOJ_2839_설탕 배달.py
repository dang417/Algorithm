n = int(input())

num_list = []

for i in range(1100):
    for j in range(1100):
        if 3*i + 5*j == n:
            num_list.append(i+j)
            break
if num_list == []:
    print(-1)
else :
    print(min(num_list))
