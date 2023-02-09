end_of_world_list = []
n = int(input())
for i in range(666, 10000000):
    if '666' in str(i):
        end_of_world_list.append(i)
print(end_of_world_list[n-1])


