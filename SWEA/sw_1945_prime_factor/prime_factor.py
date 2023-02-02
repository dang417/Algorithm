n = int(input())

prime_num = []

for i in range(2, 3300):
    for j in range(2, i):
        if i == 1:
            break
        if i % j == 0:
            break
    else:
        prime_num.append(i)
print(prime_num)
for tc in range(1, n+1):
    num = int(input())
    rlt = []
    for p in prime_num[:5]:
        cnt = 0
        while num % p == 0:
            num = num / p
            cnt += 1
        rlt.append(cnt)
    print(f'#{tc} {rlt[0]} {rlt[1]} {rlt[2]} {rlt[3]} {rlt[4]}')