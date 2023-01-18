#1~10000까지
#n과 n의 각 자리수를 더해서
#그게 1~10000까지의 리스트에 포함된다면 remove
#10000까지 진행 후 출력하면
#나머지 값들은 모두 셀프넘버일 것

def d(n) :
    n = str(n)
    num_str = list(''.join(n))
    result = 0
    num_int = 0
    for i in range(len(num_str)) :
        num_int = num_int + int(num_str[i])
    result = num_int +int(n)
    return result

ans_except = []

for i in range(30000) :
    if d(i) <= 10000 :
        ans_except.append(d(i))
for j in range(10001) :
    if j not in ans_except :
        print(j)


