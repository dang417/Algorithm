m,n=map(int,input().split())

for i in range(m,n+1):
    if i==1:#1은 소수가 아니므로 제외
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0: #약수가 존재하므로 소수가 아님
            break   #더이상 검사할 필요가 없으므로 멈춤

    else:
        print(i)
'''
에라토스 테네스의 체
대상에서 각 소수의 배수에 해당하는 값들을 모두 삭제
m = a*b 에서 a,b 둘 중 하나는 반드시 m의 제곱근보다
작거나 같아야 한다
따라서 m의 제곱근 까지만 조사해도 전수조사가 가능하다
'''