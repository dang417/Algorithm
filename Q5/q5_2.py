#1~10000까지
#n과 n의 각 자리수를 더해서
#그게 1~10000까지의 리스트에 포함된다면 remove
#10000까지 진행 후 출력하면
#나머지 값들은 모두 셀프넘버일 것

ans = list(map(str,range(1, 10001)))
result = []
num1 = 0
for n in ans :
    num = list(''.join(n))
    num_n = 0
    for i in range(len(num)) :
        num_n = num_n + int(num[i])
    num1 = num_n +int(n)
    if f'{num1}' in ans :
        ans.remove(f'{num1}')
    else :
        pass

print(ans)