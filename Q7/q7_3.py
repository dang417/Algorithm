x = int(input())

for i in range(10000000000):
    while x >= 0:
        x -= i
        break
    break
print(i)
