n = int(input())
people = [0] * n
for i in range(n):
    person = list(map(int,input().split()))
    people[i] = person + [1]

for i in range(n):
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            people[i][2] += 1

for i in range(n):
    print(people[i][2], end = ' ')
