n = int(input())
rlt = 1
cnt = 0
for i in range(1, n+1):
    rlt *= i

for i in range(len(str(rlt))):
    if rlt % 10 == 0:
        cnt += 1
        rlt = rlt // 10
    else:
        break
print(cnt)
